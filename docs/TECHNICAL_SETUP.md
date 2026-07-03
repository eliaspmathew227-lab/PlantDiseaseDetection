# Technical Setup

## Local Frontend

```bash
cd frontend
npm install
npm run dev
```

## Local Backend With Trained Model

Use the ML virtual environment because it contains TensorFlow:

```bash
cd backend
../ml/.venv/bin/uvicorn app.main:app --reload --port 8000
```

## Railway Frontend Service

Root directory:

```text
frontend
```

Build command:

```bash
npm run build
```

Start command:

```bash
npm run preview -- --host 0.0.0.0 --port $PORT
```

Environment variable:

```bash
VITE_API_BASE_URL=https://YOUR-BACKEND-DOMAIN.up.railway.app
```

## Railway Backend Service

Root directory:

```text
backend
```

Start command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Required files:

```text
backend/app/models/tomato_disease_model.keras
backend/app/models/model_classes.json
```

Required backend dependencies:

```text
fastapi
uvicorn
python-multipart
pillow
tensorflow
```

If Railway does not use Python 3.11 automatically, set:

```bash
NIXPACKS_PYTHON_VERSION=3.11
```

## Important Checks

Backend health:

```text
https://YOUR-BACKEND-DOMAIN.up.railway.app/health
```

Expected response:

```json
{"status":"ok"}
```

Prediction response should include:

```json
"model_mode": "trained"
```

If it says `"mock"`, the backend did not load the CNN model. Check:
- Is `tomato_disease_model.keras` committed and deployed?
- Is `model_classes.json` committed and deployed?
- Is TensorFlow installed in backend requirements?
- Is the backend using Python 3.11?

