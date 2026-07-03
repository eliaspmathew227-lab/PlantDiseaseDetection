# Demo Script

## Before Demo

Make sure:
- Frontend Railway URL is working.
- Backend Railway `/health` endpoint returns `{"status":"ok"}`.
- Frontend environment variable `VITE_API_BASE_URL` points to the backend URL.
- Backend response returns `"model_mode": "trained"` for real CNN predictions.

## Demo Flow

1. Open the frontend web app.
2. Briefly explain the purpose:
   - "This application detects tomato leaf diseases using a CNN model."
3. Click **Choose image**.
4. Select a tomato leaf image.
5. Click **Analyze leaf**.
6. Explain the displayed result:
   - Predicted disease
   - Confidence percentage
   - Disease description
   - Symptoms
   - Prevention
   - Treatment
7. Mention that the model currently supports five classes.

## Short Explanation During Demo

"The uploaded image is sent from the React frontend to the FastAPI backend. The backend validates the image, preprocesses it to 224 by 224 pixels, and passes it to the trained CNN model. The model returns the predicted disease class and confidence score. Based on the prediction, the system displays symptoms and preventive measures from the disease knowledge base."

## Possible Questions and Answers

Q: Which algorithm is used?
A: The project uses a CNN model with MobileNetV2 transfer learning.

Q: Why use transfer learning?
A: Transfer learning improves performance with limited data by using features learned from a large image dataset.

Q: What is the accuracy?
A: The model achieved around 89.5 percent validation accuracy.

Q: Which class needs improvement?
A: Early Blight has lower recall compared with the other classes.

Q: Can this be used directly by farmers?
A: It can be used as a first-level support tool, but expert confirmation is recommended for serious crop decisions.

Q: Why is backend needed?
A: The backend handles image upload, model loading, prediction, and disease information lookup.

Q: Can it work on mobile?
A: The web app can be opened on mobile browsers, and future work can include a TensorFlow Lite mobile app.

