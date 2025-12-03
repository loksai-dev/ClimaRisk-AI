"""Database models"""
from app.db.models.property import Property
from app.db.models.climate_data import ClimateData, RiskScore, Forecast

__all__ = ["Property", "ClimateData", "RiskScore", "Forecast"]

