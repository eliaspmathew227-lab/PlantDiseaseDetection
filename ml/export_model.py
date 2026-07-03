from pathlib import Path

import tensorflow as tf

MODEL_PATH = Path("../backend/app/models/tomato_disease_model.keras")
TFLITE_PATH = Path("../backend/app/models/tomato_disease_model.tflite")


def main():
    model = tf.keras.models.load_model(MODEL_PATH)
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()
    TFLITE_PATH.write_bytes(tflite_model)
    print(f"Exported TensorFlow Lite model to {TFLITE_PATH}")


if __name__ == "__main__":
    main()

