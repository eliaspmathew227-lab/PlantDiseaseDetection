# Tomato Disease Detector

An AI-assisted tomato leaf disease monitoring MVP. The app lets a user upload a tomato leaf image, predicts whether the plant is healthy or affected by a supported disease, and returns symptoms, prevention, and treatment guidance.

Supported classes:

- Healthy
- Early Blight
- Late Blight
- Septoria Leaf Spot
- Bacterial Spot

## Project Structure

```text
backend/   FastAPI prediction API and disease information service
frontend/  Vite + React user interface
ml/        Training, evaluation, preprocessing, and export scripts
```

## Run Backend

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Prediction API:

```http
POST http://localhost:8000/predict
```

## Run Frontend

```bash
cd frontend
npm install
npm run dev
```

Open the URL printed by Vite, usually `http://localhost:5173`.

## Model Status

The backend uses the trained model when both files exist:

```text
backend/app/models/tomato_disease_model.keras
backend/app/models/model_classes.json
```

If TensorFlow is not installed in the environment running the backend, the API falls back to deterministic mock mode. After training, run the backend with the ML virtual environment to serve real predictions:

```bash
cd backend
../ml/.venv/bin/uvicorn app.main:app --reload --port 8000
```

## ML Workflow

Dataset layout expected by the scripts:

```text
ml/datasets/
  Tomato___healthy/
  Tomato___Early_blight/
  Tomato___Late_blight/
  Tomato___Septoria_leaf_spot/
  Tomato___Bacterial_spot/
```

Train:

```bash
cd ml
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python train.py
```

Evaluate:

```bash
python evaluate.py
```
