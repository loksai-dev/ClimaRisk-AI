"""
Tests for ML models
"""
import pytest
from app.ml.models.flood_model import FloodRiskModel
from app.ml.models.heat_model import HeatRiskModel
from app.ml.models.drought_model import DroughtRiskModel
from app.ml.models.groundwater_model import GroundwaterRiskModel


def test_flood_model():
    """Test flood risk model"""
    model = FloodRiskModel()
    score = model.predict(latitude=28.6139, longitude=77.2090)
    
    assert 0 <= score <= 100
    assert isinstance(score, (int, float))


def test_heat_model():
    """Test heat risk model"""
    model = HeatRiskModel()
    score = model.predict(latitude=28.6139, longitude=77.2090)
    
    assert 0 <= score <= 100
    assert isinstance(score, (int, float))


def test_drought_model():
    """Test drought risk model"""
    model = DroughtRiskModel()
    score = model.predict(latitude=28.6139, longitude=77.2090)
    
    assert 0 <= score <= 100
    assert isinstance(score, (int, float))


def test_groundwater_model():
    """Test groundwater risk model"""
    model = GroundwaterRiskModel()
    score = model.predict(latitude=28.6139, longitude=77.2090)
    
    assert 0 <= score <= 100
    assert isinstance(score, (int, float))

