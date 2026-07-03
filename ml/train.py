import json
from pathlib import Path

import tensorflow as tf

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 10
VALIDATION_SPLIT = 0.2
SEED = 1337
DATASET_ROOT = Path("datasets")
OUTPUT_PATH = Path("../backend/app/models/tomato_disease_model.keras")
CLASSES_OUTPUT_PATH = Path("../backend/app/models/model_classes.json")

DISPLAY_LABELS = {
    "Tomato___healthy": "Healthy",
    "Tomato___Early_blight": "Early Blight",
    "Tomato___Late_blight": "Late Blight",
    "Tomato___Septoria_leaf_spot": "Septoria Leaf Spot",
    "Tomato___Bacterial_spot": "Bacterial Spot",
}


def build_model(num_classes: int):
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(*IMAGE_SIZE, 3),
        include_top=False,
        weights="imagenet",
    )
    base_model.trainable = False

    inputs = tf.keras.Input(shape=(*IMAGE_SIZE, 3))
    x = tf.keras.applications.mobilenet_v2.preprocess_input(inputs)
    x = base_model(x, training=False)
    x = tf.keras.layers.GlobalAveragePooling2D()(x)
    x = tf.keras.layers.Dropout(0.25)(x)
    outputs = tf.keras.layers.Dense(num_classes, activation="softmax")(x)
    return tf.keras.Model(inputs, outputs)


def main():
    if not DATASET_ROOT.exists():
        raise FileNotFoundError(f"Dataset folder not found: {DATASET_ROOT.resolve()}")

    train_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_ROOT,
        validation_split=VALIDATION_SPLIT,
        subset="training",
        seed=SEED,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        DATASET_ROOT,
        validation_split=VALIDATION_SPLIT,
        subset="validation",
        seed=SEED,
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
    )

    class_names = train_ds.class_names
    train_ds = train_ds.prefetch(tf.data.AUTOTUNE)
    val_ds = val_ds.prefetch(tf.data.AUTOTUNE)

    data_augmentation = tf.keras.Sequential(
        [
            tf.keras.layers.RandomFlip("horizontal"),
            tf.keras.layers.RandomRotation(0.08),
            tf.keras.layers.RandomZoom(0.1),
            tf.keras.layers.RandomBrightness(0.1),
        ]
    )

    model = build_model(len(class_names))
    model = tf.keras.Sequential([data_augmentation, model])
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0003),
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    callbacks = [
        tf.keras.callbacks.EarlyStopping(patience=3, restore_best_weights=True),
        tf.keras.callbacks.ModelCheckpoint(OUTPUT_PATH, save_best_only=True),
    ]

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS, callbacks=callbacks)
    model.save(OUTPUT_PATH)
    display_labels = [DISPLAY_LABELS.get(class_name, class_name) for class_name in class_names]
    CLASSES_OUTPUT_PATH.write_text(json.dumps(display_labels, indent=2), encoding="utf-8")
    print(f"Saved model to {OUTPUT_PATH}")
    print(f"Saved class labels to {CLASSES_OUTPUT_PATH}")
    print(f"Folder class order: {class_names}")
    print(f"Display class order: {display_labels}")


if __name__ == "__main__":
    main()
