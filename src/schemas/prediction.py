from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    """
    Validates the incoming data from the user.
    """
    text: str = Field(
        ..., 
        min_length=5, 
        max_length=5000, 
        description="The text to analyze."
    )
    # The '...' means this field is required.

class PredictionResponse(BaseModel):
    """
    Defines the exact structure of our API's output.
    """
    original_text: str
    prediction: str
    confidence_score: float
    model_version: str
