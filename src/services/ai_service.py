import asyncio
import random
from src.core.config import settings

class AIService:
    """
    A mock AI service simulating model inference.
    In a real app, you would load PyTorch/Transformers models here.
    """
    def __init__(self):
        # Pretend we are loading a heavy model into memory
        self.model_version = settings.VERSION
        self.is_loaded = True

    async def predict(self, text: str) -> dict:
        """
        Simulate an asynchronous AI prediction.
        """
        if not self.is_loaded:
            raise RuntimeError("Model is not loaded into memory.")
        
        # Simulate the time it takes for an LLM/Model to process
        await asyncio.sleep(0.5) 

        # Mock logic: if text has the word 'urgent', it's high priority
        is_urgent = "urgent" in text.lower()
        
        return {
            "prediction": "High Priority" if is_urgent else "Standard Priority",
            "confidence_score": round(random.uniform(0.75, 0.99), 2),
            "model_version": self.model_version
        }

# Create a singleton instance of the service
# This ensures we don't load the model into memory on every single API request
ai_service_instance = AIService()

def get_ai_service() -> AIService:
    """
    Dependency Injection provider.
    Allows FastAPI to inject the service into our endpoints.
    """
    return ai_service_instance
