import json
from functools import lru_cache
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "disease_info.json"


@lru_cache(maxsize=1)
def load_disease_info():
    with DATA_PATH.open("r", encoding="utf-8") as data_file:
        return json.load(data_file)


def get_disease_info(class_name: str):
    disease_info = load_disease_info()
    return disease_info.get(
        class_name,
        {
            "description": "No disease information is available for this prediction.",
            "symptoms": [],
            "prevention": [],
            "treatment": [],
            "consult_expert": "Consult a local agricultural expert if symptoms continue.",
        },
    )

