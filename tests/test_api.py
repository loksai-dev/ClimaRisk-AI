"""
Tests for API endpoints
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert "ClimaRisk AI" in response.json()["name"]


def test_health_endpoint():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_score_endpoint():
    """Test risk score endpoint"""
    payload = {
        "latitude": 28.6139,
        "longitude": 77.2090,
        "property_type": "residential"
    }
    response = client.post("/api/v1/score", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "clima_risk_score" in data
    assert 0 <= data["clima_risk_score"] <= 100


def test_forecast_endpoint():
    """Test forecast endpoint"""
    payload = {
        "latitude": 28.6139,
        "longitude": 77.2090,
        "years": [5, 10, 15]
    }
    response = client.post("/api/v1/forecast", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "forecasts" in data
    assert len(data["forecasts"]) == 3

