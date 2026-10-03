from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    Application configuration managed via Pydantic.
    Reads from environment variables or a .env file.
    """
    PROJECT_NAME: str = "Production AI Microservice"
    VERSION: str = "0.1.0"
    API_V1_STR: str = "/api/v1"
    
    # Model configuration (example)
    MODEL_PATH: str = "models/default_model.bin"
    MAX_SEQUENCE_LENGTH: int = 512
    
    # Pydantic V2 config pattern
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        case_sensitive=True
    )

# Instantiate a global settings object to be imported across the app
settings = Settings()
