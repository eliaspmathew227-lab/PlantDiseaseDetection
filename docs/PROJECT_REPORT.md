# Tomato Disease Monitoring Using Artificial Intelligence and Machine Learning

## Abstract

Plant diseases reduce agricultural productivity and crop quality. Tomato crops are commonly affected by leaf diseases such as Early Blight, Late Blight, Septoria Leaf Spot, and Bacterial Spot. Manual disease identification requires expert knowledge and can be slow for farmers. This project proposes a web-based tomato disease detection system using Artificial Intelligence and Machine Learning.

The system allows a user to upload a tomato leaf image. A Convolutional Neural Network based model predicts whether the leaf is healthy or affected by one of the supported diseases. The application then displays the predicted disease, confidence score, symptoms, prevention methods, and treatment suggestions. The project demonstrates how AI can support smart agriculture by helping farmers identify crop diseases at an early stage.

## Problem Statement

Tomato plants are vulnerable to multiple leaf diseases that can spread quickly if not detected early. Farmers may not always have immediate access to agricultural experts. This delay can lead to crop loss, reduced yield, and increased treatment cost.

The aim of this project is to develop an AI-based system that can identify common tomato leaf diseases from images and provide useful guidance to farmers.

## Objectives

- Detect tomato leaf diseases using image classification.
- Classify images into five categories:
  - Healthy
  - Early Blight
  - Late Blight
  - Septoria Leaf Spot
  - Bacterial Spot
- Build a web interface for image upload and result display.
- Provide disease information, symptoms, prevention, and treatment suggestions.
- Deploy the frontend and backend as web services.

## Scope

The project focuses on tomato leaf disease classification using image-based machine learning. It does not replace professional agricultural diagnosis, but it provides a useful first-level screening tool. The current system supports five classes and can be extended to include more crops and diseases in the future.

## Existing System

Traditional disease detection is usually done by visual inspection. This depends on the availability and experience of farmers or agricultural experts. The process may be slow and subjective. In some cases, diseases are identified only after they spread significantly.

## Proposed System

The proposed system uses a CNN-based deep learning model to classify tomato leaf images. The user uploads an image through a web application. The backend receives the image, preprocesses it, loads the trained model, and returns the predicted disease class with confidence. The frontend displays the result and related disease information.

## System Architecture

```mermaid
flowchart LR
    A["User uploads tomato leaf image"] --> B["React frontend"]
    B --> C["FastAPI backend /predict endpoint"]
    C --> D["Image validation and preprocessing"]
    D --> E["Trained CNN model"]
    E --> F["Disease prediction and confidence"]
    F --> G["Disease information JSON"]
    G --> H["Result displayed to user"]
```

## Technologies Used

Frontend:
- React
- Vite
- CSS

Backend:
- Python
- FastAPI
- Uvicorn
- Pillow

Machine Learning:
- TensorFlow / Keras
- MobileNetV2 transfer learning
- NumPy
- Scikit-learn

Deployment:
- Railway for frontend and backend services

## Dataset

The dataset contains tomato leaf images divided into five disease categories:

| Class | Images |
|---|---:|
| Bacterial Spot | 1702 |
| Early Blight | 800 |
| Late Blight | 1527 |
| Septoria Leaf Spot | 1417 |
| Healthy | 1273 |
| Total | 6719 |

The dataset was split using an 80 percent training and 20 percent validation split during model training.

## Model Development

The model uses transfer learning with MobileNetV2. MobileNetV2 is a lightweight CNN architecture suitable for image classification tasks and efficient deployment. The pretrained base model is used for feature extraction, and a custom classification head is trained for the five tomato leaf classes.

Image preprocessing:
- Resize image to 224 x 224 pixels.
- Convert image to RGB.
- Apply MobileNetV2 preprocessing.

Data augmentation:
- Random horizontal flip
- Random rotation
- Random zoom
- Random brightness adjustment

Model output:
- Disease class name
- Confidence percentage

## Training Result

The final trained model achieved approximately:

| Metric | Value |
|---|---:|
| Validation Accuracy | 89.5% |
| Weighted F1-score | 89% |
| Macro F1-score | 86% |

Per-class validation performance:

| Class | Precision | Recall | F1-score |
|---|---:|---:|---:|
| Bacterial Spot | 0.89 | 0.94 | 0.92 |
| Early Blight | 0.88 | 0.50 | 0.64 |
| Late Blight | 0.88 | 0.95 | 0.92 |
| Septoria Leaf Spot | 0.87 | 0.90 | 0.88 |
| Healthy | 0.94 | 1.00 | 0.97 |

Observation:
The model performs well overall, especially for Healthy, Late Blight, and Bacterial Spot classes. Early Blight has lower recall, which means more training images or fine-tuning may be required to improve its detection.

## Implementation Details

Frontend:
- Provides an image upload interface.
- Shows preview of selected image.
- Sends image to backend API using `POST /predict`.
- Displays prediction, confidence, symptoms, prevention, and treatment.

Backend:
- Accepts image files in JPEG, PNG, or WebP format.
- Validates image size and format.
- Loads the trained TensorFlow/Keras model when available.
- Falls back to mock mode only if the trained model or TensorFlow runtime is missing.
- Returns structured JSON response.

Disease information:
- Stored in `backend/app/data/disease_info.json`.
- Contains description, symptoms, prevention, treatment, and expert consultation advice.

## API Design

Endpoint:

```http
POST /predict
```

Input:
- Image file uploaded as multipart form data.

Sample response:

```json
{
  "prediction": "Healthy",
  "confidence": 99.53,
  "model_mode": "trained",
  "description": "The uploaded leaf appears healthy based on the current prediction.",
  "symptoms": ["Uniform green leaf color"],
  "prevention": ["Inspect plants regularly"],
  "treatment": ["No disease treatment is needed"]
}
```

Health check endpoint:

```http
GET /health
```

## Testing

The system was tested at multiple levels:

- Frontend build test using `npm run build`.
- Backend syntax validation using Python compile checks.
- Model evaluation using validation dataset.
- API smoke test using a tomato leaf image.
- Deployment testing on Railway.

## Advantages

- Helps identify tomato diseases at an early stage.
- Provides quick prediction from leaf images.
- User-friendly web interface.
- Lightweight CNN model suitable for deployment.
- Can be extended to support more crops and diseases.

## Limitations

- Accuracy depends on image quality and dataset diversity.
- Current system supports only tomato leaves and five classes.
- Similar diseases may be confused, especially Early Blight.
- The model should be validated with real field images before agricultural use.
- It provides guidance, not a replacement for expert diagnosis.

## Future Enhancements

- Add camera capture from mobile devices.
- Improve Early Blight classification using more data and fine-tuning.
- Add multilingual disease guidance for farmers.
- Store prediction history.
- Add Grad-CAM heatmaps to explain model decisions.
- Convert model to TensorFlow Lite for mobile deployment.
- Extend the system to other crops such as potato, rice, and chilli.

## Conclusion

This project demonstrates the use of AI and ML in smart agriculture. By combining a CNN-based image classification model with a simple web application, the system can detect common tomato leaf diseases and provide useful recommendations. The project shows how deep learning can be applied to real-world agricultural problems and can be further improved for practical field use.

