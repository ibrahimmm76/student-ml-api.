from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    
    # All assertions must be inside the function like this:
    assert data["status"] == "healthy"
    assert data["application"] == "student-ml-api"
    assert data["application_version"] == "1.1.0"
    assert data["model version"] == "model-1"
def test_successful_predict():
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200
    assert response.json() == {"input": 10.0, "prediction": 20.0}

def test_missing_input():
    # Sending an empty JSON body
    response = client.post("/predict", json={})
    assert response.status_code == 422 # Unprocessable Entity

def test_invalid_input():
    # Sending a string instead of a number
    response = client.post("/predict", json={"value": "not-a-number"})
    assert response.status_code == 422