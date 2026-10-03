from fastapi import APIRouter
from src.core.config import settings

# A dedicated router for health checks
router = APIRouter()

@router.get("/health", tags=["System"])
async def health_check() -> dict[str, str]:
    """
    Health check endpoint for load balancers and Kubernetes.
    Returns the basic health status and version of the API.
    """
    return {
        "status": "healthy",
        "service": settings.PROJECT_NAME,
        "version": settings.VERSION
    }
