from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="student-ml-api")

class PredictionInput(BaseModel):
    value: float

@app.get("/health") # (or @app.route if using Flask)
def health_check():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "application_version": "1.1.0",
        "model version": "model-1"
    }
@app.post("/predict")
def predict(data: PredictionInput):
    # The assignment just requires a simple mathematical prediction
    prediction_result = data.value * 2 
    return {
        "input": data.value,
        "prediction": prediction_result
    }