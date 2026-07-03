import hashlib
import json
from io import BytesIO
from pathlib import Path

from PIL import Image

SUPPORTED_CLASSES = [
    "Healthy",
    "Early Blight",
    "Late Blight",
    "Septoria Leaf Spot",
    "Bacterial Spot",
]

MODEL_PATH = Path(__file__).resolve().parents[1] / "models" / "tomato_disease_model.keras"
CLASSES_PATH = Path(__file__).resolve().parents[1] / "models" / "model_classes.json"
IMAGE_SIZE = (224, 224)

_loaded_model = None
_loaded_classes = None


def _load_model():
    global _loaded_model, _loaded_classes

    if _loaded_model is not None:
        return _loaded_model, _loaded_classes

    if not MODEL_PATH.exists() or not CLASSES_PATH.exists():
        return None, None

    try:
        import tensorflow as tf
    except ImportError:
        return None, None

    _loaded_model = tf.keras.models.load_model(MODEL_PATH)
    _loaded_classes = json.loads(CLASSES_PATH.read_text(encoding="utf-8"))
    return _loaded_model, _loaded_classes


def _predict_with_trained_model(image_bytes: bytes):
    import numpy as np

    model, class_names = _load_model()
    if model is None or class_names is None:
        return None

    image = Image.open(BytesIO(image_bytes)).convert("RGB").resize(IMAGE_SIZE)
    image_array = np.asarray(image, dtype=np.float32)
    batch = np.expand_dims(image_array, axis=0)
    probabilities = model.predict(batch, verbose=0)[0]
    class_index = int(np.argmax(probabilities))

    return {
        "class_name": class_names[class_index],
        "confidence": round(float(probabilities[class_index]) * 100, 2),
        "model_mode": "trained",
    }


def predict_image(image_bytes: bytes, filename: str):
    trained_prediction = _predict_with_trained_model(image_bytes)
    if trained_prediction:
        return trained_prediction

    digest = hashlib.sha256(image_bytes + filename.encode("utf-8")).digest()
    class_index = digest[0] % len(SUPPORTED_CLASSES)
    confidence = 72 + (digest[1] % 2400) / 100

    return {
        "class_name": SUPPORTED_CLASSES[class_index],
        "confidence": round(min(confidence, 96.0), 2),
        "model_mode": "mock",
    }
