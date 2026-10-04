import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="module")
def client():
    """
    Creates a FastAPI TestClient fixture.
    This allows us to simulate HTTP requests without actually starting a live server.
    """
    with TestClient(app) as c:
        yield c
