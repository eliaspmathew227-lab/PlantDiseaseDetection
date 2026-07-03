from pathlib import Path

DATASET_ROOT = Path("datasets")
CLASS_NAMES = [
    "Tomato___healthy",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Bacterial_spot",
]


def validate_dataset():
    missing = []
    for class_name in CLASS_NAMES:
        class_dir = DATASET_ROOT / class_name
        if not class_dir.exists():
            missing.append(str(class_dir))

    if missing:
        print("Missing dataset folders:")
        for path in missing:
            print(f"- {path}")
        return False

    print("Dataset folder structure is valid.")
    return True


if __name__ == "__main__":
    validate_dataset()
