import json
from pathlib import Path

import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
VALIDATION_SPLIT = 0.2
SEED = 1337
DATASET_ROOT = Path("datasets")
MODEL_PATH = Path("../backend/app/models/tomato_disease_model.keras")
CLASSES_PATH = Path("../backend/app/models/model_classes.json")


def main():
    test_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_ROOT,
        validation_split=VALIDATION_SPLIT,
        subset="validation",
        seed=SEED,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=True,
    )
    class_names = json.loads(CLASSES_PATH.read_text(encoding="utf-8"))
    model = tf.keras.models.load_model(MODEL_PATH)

    true_batches = []
    prediction_batches = []

    for images, labels in test_ds:
        probabilities = model.predict(images, verbose=0)
        true_batches.append(labels.numpy())
        prediction_batches.append(np.argmax(probabilities, axis=1))

    y_true = np.concatenate(true_batches)
    y_pred = np.concatenate(prediction_batches)

    print(classification_report(y_true, y_pred, target_names=class_names))
    print("Confusion matrix:")
    print(confusion_matrix(y_true, y_pred))


if __name__ == "__main__":
    main()
