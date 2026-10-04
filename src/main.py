import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.config import settings
from src.api import health, predict

def get_application() -> FastAPI:
    """
    Application factory pattern. This makes testing easier and 
    keeps the app instance configuration modular.
    """
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Set all CORS enabled origins (Industry standard for APIs)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], # In production, restrict this to specific domains
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(health.router, prefix=settings.API_V1_STR)
    app.include_router(predict.router, prefix=settings.API_V1_STR)

    return app

app = get_application()

if __name__ == "__main__":
    # This block allows running the file directly for debugging
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)
