from io import BytesIO

from fastapi import APIRouter, File, HTTPException, UploadFile
from PIL import Image, UnidentifiedImageError

from app.services.disease_info_service import get_disease_info
from app.services.model_service import predict_image

router = APIRouter(tags=["prediction"])

ALLOWED_CONTENT_TYPES = {"image/jpeg", "image/png", "image/webp"}
MAX_IMAGE_BYTES = 8 * 1024 * 1024


@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail="Upload a JPEG, PNG, or WebP tomato leaf image.",
        )

    raw_image = await file.read()
    if not raw_image:
        raise HTTPException(status_code=400, detail="Uploaded image is empty.")

    if len(raw_image) > MAX_IMAGE_BYTES:
        raise HTTPException(status_code=400, detail="Image must be smaller than 8 MB.")

    try:
        image = Image.open(BytesIO(raw_image))
        image.verify()
    except (UnidentifiedImageError, OSError):
        raise HTTPException(status_code=400, detail="Uploaded file is not a valid image.")

    prediction = predict_image(raw_image, file.filename or "leaf-image")
    disease_info = get_disease_info(prediction["class_name"])

    return {
        "prediction": prediction["class_name"],
        "confidence": prediction["confidence"],
        "model_mode": prediction["model_mode"],
        **disease_info,
    }
