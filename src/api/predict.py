from fastapi import APIRouter, Depends, HTTPException
from src.schemas.prediction import PredictionRequest, PredictionResponse
from src.services.ai_service import AIService, get_ai_service
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/predict", response_model=PredictionResponse, tags=["AI"])
async def make_prediction(
    request: PredictionRequest, 
    ai_service: AIService = Depends(get_ai_service)
):
    """
    Accepts text, passes it to the AI service, and returns the prediction.
    """
    try:
        # Call the AI service
        result = await ai_service.predict(text=request.text)
        
        # Format the response using our Pydantic schema
        return PredictionResponse(
            original_text=request.text,
            prediction=result["prediction"],
            confidence_score=result["confidence_score"],
            model_version=result["model_version"]
        )
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        # Never expose raw internal errors to the user in production
        raise HTTPException(status_code=500, detail="Internal server error during prediction.")
