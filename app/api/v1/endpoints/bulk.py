"""
Bulk Scoring Endpoint for Enterprise Users
Allows scoring multiple properties in a single request
"""
from fastapi import APIRouter, HTTPException
from typing import List
from pydantic import BaseModel, Field

from app.db.schemas.score import ScoreResponse, RiskBreakdown
from app.ml.ensemble import EnsembleScorer

router = APIRouter()

ensemble_scorer = EnsembleScorer()


class PropertyLocation(BaseModel):
    """Single property location for bulk scoring"""
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    property_type: str = Field(default="residential")
    property_id: str = Field(default="", description="Optional identifier")


class BulkScoreRequest(BaseModel):
    """Request for bulk scoring"""
    properties: List[PropertyLocation] = Field(..., min_items=1, max_items=1000)


class BulkScoreResponse(BaseModel):
    """Response for bulk scoring"""
    total_properties: int
    successful: int
    failed: int
    scores: List[dict]


@router.post("/bulk-scoring", response_model=BulkScoreResponse)
async def bulk_score(request: BulkScoreRequest):
    """
    Score multiple properties in bulk
    
    - **properties**: List of property locations (max 1000)
    
    Useful for banks, insurance companies, and real estate platforms
    that need to assess multiple properties at once.
    """
    if len(request.properties) > 1000:
        raise HTTPException(
            status_code=400,
            detail="Maximum 1000 properties per request"
        )
    
    scores = []
    successful = 0
    failed = 0
    
    for prop in request.properties:
        try:
            # Calculate score
            result = ensemble_scorer.calculate_score(
                latitude=prop.latitude,
                longitude=prop.longitude,
                property_type=prop.property_type,
            )
            
            # Format response
            score_data = {
                "property_id": prop.property_id or "",
                "latitude": prop.latitude,
                "longitude": prop.longitude,
                "clima_risk_score": result['clima_risk_score'],
                "risk_breakdown": result['risk_breakdown'],
                "risk_level": result['risk_level'],
                "confidence": result['confidence'],
                "calculated_at": result['calculated_at'],
            }
            
            scores.append(score_data)
            successful += 1
        
        except Exception as e:
            failed += 1
            scores.append({
                "property_id": prop.property_id or "",
                "latitude": prop.latitude,
                "longitude": prop.longitude,
                "error": str(e)
            })
    
    return BulkScoreResponse(
        total_properties=len(request.properties),
        successful=successful,
        failed=failed,
        scores=scores,
    )

