from src.main import app
from src.services.ai_service import get_ai_service

class MockAIService:
    """
    A fake version of our AI service that returns instant, predictable results.
    """
    async def predict(self, text: str) -> dict:
        return {
            "prediction": "Mocked Priority",
            "confidence_score": 0.99,
            "model_version": "test-v1"
        }

def get_mock_ai_service():
    return MockAIService()

# The Senior Magic: Swap out the real model for the fake one!
app.dependency_overrides[get_ai_service] = get_mock_ai_service

def test_predict_endpoint_success(client):
    """
    Test that a valid request returns the mocked AI response.
    """
    payload = {"text": "This is a valid test document."}
    response = client.post("/api/v1/predict", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["prediction"] == "Mocked Priority"
    assert data["confidence_score"] == 0.99

def test_predict_endpoint_validation_error(client):
    """
    Test that our Pydantic schema correctly rejects bad data.
    """
    # Text is less than 5 characters (our schema requires min_length=5)
    payload = {"text": "Hi"} 
    response = client.post("/api/v1/predict", json=payload)
    
    # 422 is the HTTP status code for 'Unprocessable Entity' (Validation Error)
    assert response.status_code == 422 
