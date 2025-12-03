"""
Risk Scoring Endpoint
"""
from fastapi import APIRouter, HTTPException

from app.db.schemas.score import ScoreRequest, ScoreResponse, RiskBreakdown
from app.ml.ensemble import EnsembleScorer

router = APIRouter()

# Initialize ensemble scorer (in production, this would be a singleton)
ensemble_scorer = EnsembleScorer()


@router.post("", response_model=ScoreResponse)
async def calculate_risk_score(request: ScoreRequest):
    """
    Calculate climate risk score for a location
    
    - **latitude**: Latitude of the location (-90 to 90)
    - **longitude**: Longitude of the location (-180 to 180)
    - **property_type**: Type of property (residential, commercial, industrial, agricultural)
    - **area_sqm**: Area in square meters (optional)
    - **floor**: Floor number (optional)
    
    Returns comprehensive climate risk score with breakdown by risk type.
    """
    try:
        # Calculate score using ensemble model
        result = ensemble_scorer.calculate_score(
            latitude=request.latitude,
            longitude=request.longitude,
            property_type=request.property_type,
            area_sqm=request.area_sqm,
            floor=request.floor,
        )
        
        # Format response
        return ScoreResponse(
            clima_risk_score=result['clima_risk_score'],
            risk_breakdown=RiskBreakdown(**result['risk_breakdown']),
            risk_level=result['risk_level'],
            confidence=result['confidence'],
            latitude=request.latitude,
            longitude=request.longitude,
            calculated_at=result['calculated_at'],
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error calculating risk score: {str(e)}"
        )

