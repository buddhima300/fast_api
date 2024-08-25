from fastapi.testclient import TestClient
from app import app  # Adjust this import if your file is named differently

client = TestClient(app)

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Best university courses recommendation machine learning API"}
