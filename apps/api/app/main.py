from fastapi import FastAPI
from app.api.webhook import router as webhook_router

app = FastAPI(title="SLAIVO CARGO OS API")

app.include_router(webhook_router)


@app.get("/")
def root():
    return {"status": "SLAIVO API running"}