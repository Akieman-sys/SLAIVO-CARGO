import json
from sqlalchemy import text
from app.db.database import engine


def insert_raw_message(org_id: str, phone: str, text_msg: str, payload: dict):
    with engine.connect() as conn:
        conn.execute(
            text("""
                insert into messages_raw (
                    org_id,
                    sender_phone,
                    message_text,
                    raw_payload
                )
                values (
                    :org_id,
                    :phone,
                    :text_msg,
                    CAST(:payload AS jsonb)
                )
            """),
            {
                "org_id": org_id,
                "phone": phone,
                "text_msg": text_msg,
                "payload": json.dumps(payload),
            }
        )
        conn.commit()