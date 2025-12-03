"""
Pydantic schemas for risk scoring
"""
from typing import Optional, Literal
from pydantic import BaseModel, Field


class RiskBreakdown(BaseModel):
    """Breakdown of individual risk scores"""
    flood: float = Field(..., ge=0, le=100, description="Flood risk score (0-100)")
    heat: float = Field(..., ge=0, le=100, description="Heat risk score (0-100)")
    drought: float = Field(..., ge=0, le=100, description="Drought risk score (0-100)")
    groundwater: float = Field(..., ge=0, le=100, description="Groundwater risk score (0-100)")
    rainfall: float = Field(..., ge=0, le=100, description="Rainfall risk score (0-100)")


class ScoreRequest(BaseModel):
    """Request schema for risk score calculation"""
    latitude: float = Field(..., ge=-90, le=90, description="Latitude")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude")
    property_type: Optional[Literal["residential", "commercial", "industrial", "agricultural"]] = Field(
        default="residential",
        description="Type of property"
    )
    area_sqm: Optional[float] = Field(None, gt=0, description="Area in square meters")
    floor: Optional[int] = Field(None, ge=0, description="Floor number")


class ScoreResponse(BaseModel):
    """Response schema for risk score"""
    clima_risk_score: float = Field(..., ge=0, le=100, description="Overall climate risk score (0-100)")
    risk_breakdown: RiskBreakdown = Field(..., description="Individual risk scores")
    risk_level: Literal["low", "moderate", "high", "extreme"] = Field(..., description="Risk level")
    confidence: float = Field(..., ge=0, le=1, description="Confidence score (0-1)")
    latitude: float = Field(..., description="Latitude of scored location")
    longitude: float = Field(..., description="Longitude of scored location")
    calculated_at: str = Field(..., description="ISO timestamp of calculation")

