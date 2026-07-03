import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.prediction import router as prediction_router


def get_allowed_origins():
    default_origins = [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://pleasing-adaptation-production-2d6a.up.railway.app",
    ]
    extra_origins = os.getenv("FRONTEND_ORIGINS", "")
    configured_origins = [
        origin.strip()
        for origin in extra_origins.split(",")
        if origin.strip()
    ]
    return default_origins + configured_origins

app = FastAPI(
    title="Tomato Disease Detector API",
    description="Predict tomato leaf disease from uploaded images.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=get_allowed_origins(),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
