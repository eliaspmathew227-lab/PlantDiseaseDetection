from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.prediction import router as prediction_router

app = FastAPI(
    title="Tomato Disease Detector API",
    description="Predict tomato leaf disease from uploaded images.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(prediction_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
