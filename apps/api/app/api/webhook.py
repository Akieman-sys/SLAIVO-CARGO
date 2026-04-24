from datetime import datetime, timezone
from fastapi import APIRouter, Request

from app.models.message import NormalizedMessage

router = APIRouter()


@router.get("/webhook/whatsapp")
def verify_webhook():
    return {"status": "webhook verification endpoint ready"}


def normalize_whatsapp_payload(payload: dict) -> NormalizedMessage:
    from_phone = payload.get("from", "unknown")
    to_phone = payload.get("to")
    text_body = payload.get("text")
    provider_message_id = payload.get("id")

    dedupe_key = provider_message_id or f"whatsapp:{from_phone}:{text_body}"

    return NormalizedMessage(
        provider_message_id=provider_message_id,
        from_phone=from_phone,
        to_phone=to_phone,
        text_body=text_body,
        received_at=datetime.now(timezone.utc),
        dedupe_key=dedupe_key,
    )


@router.post("/webhook/whatsapp")
async def receive_whatsapp_message(request: Request):
    payload = await request.json()

    normalized_message = normalize_whatsapp_payload(payload)

    print("=== WHATSAPP WEBHOOK RECEIVED ===")
    print(payload)

    print("=== NORMALIZED MESSAGE ===")
    print(normalized_message.model_dump())

    return {
        "status": "received",
        "normalized_message": normalized_message.model_dump(mode="json"),
    }