# Presentation Outline

## Slide 1: Title

Tomato Disease Monitoring Using Artificial Intelligence and Machine Learning

Presented by:
- Team members
- Department
- Institution

## Slide 2: Introduction

- Tomato is an important agricultural crop.
- Leaf diseases reduce crop yield and quality.
- Early detection helps farmers take preventive action.
- AI-based image classification can support disease identification.

## Slide 3: Problem Statement

Farmers may not always identify tomato diseases early or accurately. Manual inspection depends on expert availability and experience. This project solves the problem by detecting tomato leaf diseases from images.

## Slide 4: Objectives

- Build an AI-based tomato disease detector.
- Classify leaf images into five categories.
- Display confidence score and disease information.
- Provide symptoms, prevention, and treatment guidance.
- Deploy the system as a web application.

## Slide 5: Supported Classes

- Healthy
- Early Blight
- Late Blight
- Septoria Leaf Spot
- Bacterial Spot

## Slide 6: System Architecture

Show this flow:

User image upload → React frontend → FastAPI backend → Image preprocessing → CNN model → Disease information → Result page

## Slide 7: Dataset

- Total images: 6719
- Classes: 5
- Train/validation split: 80/20

Dataset distribution:
- Bacterial Spot: 1702
- Early Blight: 800
- Late Blight: 1527
- Septoria Leaf Spot: 1417
- Healthy: 1273

## Slide 8: Machine Learning Model

- Model type: CNN image classifier
- Architecture: MobileNetV2 transfer learning
- Input size: 224 x 224
- Output: predicted class and confidence
- Data augmentation used to improve generalization

## Slide 9: Implementation

Frontend:
- React + Vite
- Image upload and result UI

Backend:
- FastAPI
- `/predict` endpoint
- TensorFlow/Keras model inference

Data:
- Disease recommendations stored in JSON

## Slide 10: Result

Validation accuracy: 89.5%

Strong classes:
- Healthy
- Late Blight
- Bacterial Spot

Needs improvement:
- Early Blight recall

## Slide 11: Demo

Demo steps:
- Open deployed frontend.
- Upload tomato leaf image.
- Click analyze.
- Show prediction, confidence, and recommendations.

## Slide 12: Advantages

- Fast disease prediction.
- Farmer-friendly interface.
- Gives preventive suggestions.
- Can reduce delay in disease identification.
- Expandable to more crops.

## Slide 13: Limitations

- Works only for supported tomato leaf classes.
- Accuracy depends on image clarity.
- Field images may differ from dataset images.
- Not a replacement for agricultural experts.

## Slide 14: Future Scope

- Add mobile camera support.
- Add multilingual guidance.
- Improve model with real field images.
- Add prediction history.
- Add explainable AI heatmaps.
- Convert to mobile app using TensorFlow Lite.

## Slide 15: Conclusion

The project successfully demonstrates AI-based tomato disease detection using CNN and web technologies. It is a practical example of applying machine learning to agriculture and can be improved into a useful farmer-support tool.

