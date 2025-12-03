"""
Pydantic schemas for forecasting
"""
from typing import List, Optional, Literal
from pydantic import BaseModel, Field, field_validator


class ForecastRequest(BaseModel):
    """Request schema for future forecast"""
    latitude: float = Field(..., ge=-90, le=90, description="Latitude")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude")
    years: List[int] = Field(
        default=[5, 10, 15, 20, 25, 30],
        description="List of years into the future to forecast"
    )
    
    @field_validator('years')
    @classmethod
    def validate_years(cls, v):
        """Validate forecast years"""
        if not v:
            raise ValueError('At least one year must be specified')
        if any(year < 1 or year > 50 for year in v):
            raise ValueError('Forecast years must be between 1 and 50')
        return sorted(set(v))  # Remove duplicates and sort


class YearForecast(BaseModel):
    """Forecast for a specific year"""
    year: int = Field(..., description="Years into the future")
    predicted_clima_risk_score: float = Field(..., ge=0, le=100)
    predicted_risk_level: Literal["low", "moderate", "high", "extreme"]
    predicted_flood_risk: float = Field(..., ge=0, le=100)
    predicted_heat_risk: float = Field(..., ge=0, le=100)
    predicted_drought_risk: float = Field(..., ge=0, le=100)
    predicted_groundwater_risk: float = Field(..., ge=0, le=100)
    predicted_rainfall_risk: float = Field(..., ge=0, le=100)
    confidence_interval_lower: Optional[float] = None
    confidence_interval_upper: Optional[float] = None


class ForecastResponse(BaseModel):
    """Response schema for forecast"""
    latitude: float = Field(..., description="Latitude")
    longitude: float = Field(..., description="Longitude")
    forecasts: List[YearForecast] = Field(..., description="Forecasts for each requested year")
    current_score: Optional[float] = Field(None, description="Current risk score for reference")
    forecasted_at: str = Field(..., description="ISO timestamp")

