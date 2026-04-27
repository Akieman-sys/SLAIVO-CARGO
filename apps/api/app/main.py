from fastapi import FastAPI
from app.api.webhook import router as webhook_router
from app.db.database import test_db_connection

app = FastAPI(title="SLAIVO CARGO OS API")

app.include_router(webhook_router)


@app.get("/")
def root():
    return {"status": "SLAIVO API running"}


@app.get("/health/db")
def db_health():
    test_db_connection()
    return {"status": "database connected"}