"""Pydantic schemas for API validation"""
from app.db.schemas.score import ScoreRequest, ScoreResponse, RiskBreakdown
from app.db.schemas.forecast import ForecastRequest, ForecastResponse
from app.db.schemas.property import PropertyAnalysisRequest, PropertyAnalysisResponse

__all__ = [
    "ScoreRequest",
    "ScoreResponse",
    "RiskBreakdown",
    "ForecastRequest",
    "ForecastResponse",
    "PropertyAnalysisRequest",
    "PropertyAnalysisResponse",
]

