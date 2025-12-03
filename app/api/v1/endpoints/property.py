"""
Property Analysis Endpoint
"""
from fastapi import APIRouter, HTTPException

from app.db.schemas.property import PropertyAnalysisRequest, PropertyAnalysisResponse
from app.db.schemas.score import ScoreResponse, RiskBreakdown
from app.ml.ensemble import EnsembleScorer

router = APIRouter()

ensemble_scorer = EnsembleScorer()


@router.post("/analysis", response_model=PropertyAnalysisResponse)
async def analyze_property(request: PropertyAnalysisRequest):
    """
    Comprehensive property analysis including risk scores and recommendations
    
    - **address**: Property address (optional, will be geocoded)
    - **latitude**: Latitude (optional if address provided)
    - **longitude**: Longitude (optional if address provided)
    - **property_details**: Additional property details (type, floor, area, etc.)
    
    Returns comprehensive analysis with risk scores, recommendations, and trends.
    """
    try:
        # Geocode address if provided (simplified - in production use geocoding service)
        if request.address and not (request.latitude and request.longitude):
            # In production: use geocoding API (Nominatim, Google Geocoding, etc.)
            raise HTTPException(
                status_code=400,
                detail="Address geocoding not implemented yet. Please provide latitude and longitude."
            )
        
        if not (request.latitude and request.longitude):
            raise HTTPException(
                status_code=400,
                detail="Either address or latitude/longitude must be provided"
            )
        
        # Extract property details
        property_type = request.property_details.get('type', 'residential')
        area_sqm = request.property_details.get('area_sqm')
        floor = request.property_details.get('floor')
        
        # Calculate risk score
        score_result = ensemble_scorer.calculate_score(
            latitude=request.latitude,
            longitude=request.longitude,
            property_type=property_type,
            area_sqm=area_sqm,
            floor=floor,
        )
        
        # Generate recommendations
        recommendations = _generate_recommendations(score_result)
        
        # Format risk score response
        risk_score = ScoreResponse(
            clima_risk_score=score_result['clima_risk_score'],
            risk_breakdown=RiskBreakdown(**score_result['risk_breakdown']),
            risk_level=score_result['risk_level'],
            confidence=score_result['confidence'],
            latitude=request.latitude,
            longitude=request.longitude,
            calculated_at=score_result['calculated_at'],
        )
        
        # In production, this would:
        # - Check if property exists in database
        # - Load historical trends
        # - Analyze nearby risks
        # - Generate property_id
        
        import uuid
        property_id = str(uuid.uuid4())
        
        return PropertyAnalysisResponse(
            property_id=property_id,
            address=request.address,
            latitude=request.latitude,
            longitude=request.longitude,
            risk_score=risk_score,
            recommendations=recommendations,
            nearby_risks=None,  # Would be populated in production
            historical_trends=None,  # Would be populated in production
        )
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error analyzing property: {str(e)}"
        )


def _generate_recommendations(score_result: dict) -> list:
    """Generate risk mitigation recommendations based on score"""
    recommendations = []
    
    risk_level = score_result['risk_level']
    breakdown = score_result['risk_breakdown']
    
    # Overall recommendations
    if risk_level == "extreme":
        recommendations.append(
            "⚠️ EXTREME RISK: Consider alternative locations or robust mitigation measures"
        )
    elif risk_level == "high":
        recommendations.append(
            "🔴 HIGH RISK: Implement comprehensive risk mitigation strategies"
        )
    
    # Specific risk recommendations
    if breakdown['flood'] > 70:
        recommendations.append(
            "💧 High flood risk: Consider elevated foundation, flood barriers, and flood insurance"
        )
    
    if breakdown['heat'] > 70:
        recommendations.append(
            "🌡️ High heat risk: Consider green roofs, insulation, and efficient cooling systems"
        )
    
    if breakdown['drought'] > 70:
        recommendations.append(
            "☀️ High drought risk: Consider water conservation systems and drought-resistant landscaping"
        )
    
    if breakdown['groundwater'] > 70:
        recommendations.append(
            "💾 High groundwater depletion risk: Consider rainwater harvesting and reduced water dependency"
        )
    
    # General recommendations
    if risk_level in ["moderate", "high", "extreme"]:
        recommendations.append(
            "📊 Monitor climate trends and update risk assessment annually"
        )
        recommendations.append(
            "🏠 Ensure property insurance covers climate-related damages"
        )
    
    return recommendations

