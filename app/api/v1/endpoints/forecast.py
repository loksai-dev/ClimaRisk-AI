"""
Forecast Endpoint
"""
from fastapi import APIRouter, HTTPException

from app.db.schemas.forecast import ForecastRequest, ForecastResponse, YearForecast
from app.ml.ensemble import EnsembleScorer

router = APIRouter()

# Initialize ensemble scorer
ensemble_scorer = EnsembleScorer()


@router.post("", response_model=ForecastResponse)
async def get_forecast(request: ForecastRequest):
    """
    Get future climate risk forecast for a location
    
    - **latitude**: Latitude of the location
    - **longitude**: Longitude of the location
    - **years**: List of years into the future to forecast (e.g., [5, 10, 15, 20, 25, 30])
    
    Returns forecasts for each requested year with predicted risk scores and confidence intervals.
    """
    try:
        # Get forecast from ensemble model
        result = ensemble_scorer.forecast(
            latitude=request.latitude,
            longitude=request.longitude,
            years=request.years,
        )
        
        # Format forecasts
        forecasts = [
            YearForecast(**forecast) for forecast in result['forecasts']
        ]
        
        return ForecastResponse(
            latitude=request.latitude,
            longitude=request.longitude,
            forecasts=forecasts,
            current_score=result.get('current_score'),
            forecasted_at=result['forecasted_at'],
        )
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating forecast: {str(e)}"
        )

