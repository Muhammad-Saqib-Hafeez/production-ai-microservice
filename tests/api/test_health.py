def test_health_check_returns_200(client):
    """
    Ensure the health check endpoint is alive and returns the expected schema.
    """
    response = client.get("/api/v1/health")
    
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "version" in data
