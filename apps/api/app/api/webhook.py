from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/webhook/whatsapp")
def verify_webhook():
    return {"status": "webhook verification endpoint ready"}


@router.post("/webhook/whatsapp")
async def receive_whatsapp_message(request: Request):
    payload = await request.json()

    print("=== WHATSAPP WEBHOOK RECEIVED ===")
    print(payload)

    return {
        "status": "received",
        "message": "WhatsApp payload received successfully"
    }