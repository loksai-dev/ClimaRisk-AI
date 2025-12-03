"""
Pydantic schemas for property analysis
"""
from typing import List, Optional, Literal
from pydantic import BaseModel, Field
from app.db.schemas.score import ScoreResponse


class PropertyAnalysisRequest(BaseModel):
    """Request schema for property analysis"""
    address: Optional[str] = Field(None, description="Property address")
    latitude: Optional[float] = Field(None, ge=-90, le=90, description="Latitude")
    longitude: Optional[float] = Field(None, ge=-180, le=180, description="Longitude")
    property_details: Optional[dict] = Field(
        default_factory=dict,
        description="Additional property details (type, floor, area, etc.)"
    )


class PropertyAnalysisResponse(BaseModel):
    """Response schema for property analysis"""
    property_id: str = Field(..., description="Unique property identifier")
    address: Optional[str] = None
    latitude: float
    longitude: float
    risk_score: ScoreResponse = Field(..., description="Current risk score")
    recommendations: List[str] = Field(default_factory=list, description="Risk mitigation recommendations")
    nearby_risks: Optional[dict] = Field(None, description="Nearby risk factors")
    historical_trends: Optional[dict] = Field(None, description="Historical risk trends")

