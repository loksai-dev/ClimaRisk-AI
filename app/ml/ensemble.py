"""
Ensemble scoring engine that combines multiple risk models
"""
from typing import Dict, Tuple
import numpy as np
from datetime import datetime

from app.ml.models.flood_model import FloodRiskModel
from app.ml.models.heat_model import HeatRiskModel
from app.ml.models.drought_model import DroughtRiskModel
from app.ml.models.groundwater_model import GroundwaterRiskModel


class EnsembleScorer:
    """
    Ensemble model that combines predictions from multiple risk models
    to generate a comprehensive ClimaRisk Score
    """
    
    def __init__(self):
        """Initialize ensemble with all risk models"""
        self.flood_model = FloodRiskModel()
        self.heat_model = HeatRiskModel()
        self.drought_model = DroughtRiskModel()
        self.groundwater_model = GroundwaterRiskModel()
        
        # Weight configuration (can be region-specific)
        # These weights determine how much each risk contributes to overall score
        self.weights = {
            'flood': 0.25,
            'heat': 0.25,
            'drought': 0.20,
            'groundwater': 0.15,
            'rainfall': 0.15,  # Derived from drought model
        }
    
    def calculate_score(
        self,
        latitude: float,
        longitude: float,
        property_type: str = "residential",
        **kwargs
    ) -> Dict:
        """
        Calculate comprehensive climate risk score
        
        Args:
            latitude: Latitude of location
            longitude: Longitude of location
            property_type: Type of property
            **kwargs: Additional parameters
            
        Returns:
            Dictionary with risk scores and breakdown
        """
        # Get predictions from individual models
        flood_score = self.flood_model.predict(latitude, longitude, **kwargs)
        heat_score = self.heat_model.predict(latitude, longitude, **kwargs)
        drought_score = self.drought_model.predict(latitude, longitude, **kwargs)
        groundwater_score = self.groundwater_model.predict(latitude, longitude, **kwargs)
        
        # Rainfall risk is derived from drought/precipitation patterns
        rainfall_score = self._calculate_rainfall_risk(
            drought_score, 
            latitude, 
            longitude
        )
        
        # Calculate weighted ensemble score
        clima_risk_score = (
            self.weights['flood'] * flood_score +
            self.weights['heat'] * heat_score +
            self.weights['drought'] * drought_score +
            self.weights['groundwater'] * groundwater_score +
            self.weights['rainfall'] * rainfall_score
        )
        
        # Determine risk level
        risk_level = self._determine_risk_level(clima_risk_score)
        
        # Calculate confidence based on model agreement
        scores = [flood_score, heat_score, drought_score, groundwater_score, rainfall_score]
        confidence = self._calculate_confidence(scores)
        
        return {
            'clima_risk_score': round(clima_risk_score, 2),
            'risk_breakdown': {
                'flood': round(flood_score, 2),
                'heat': round(heat_score, 2),
                'drought': round(drought_score, 2),
                'groundwater': round(groundwater_score, 2),
                'rainfall': round(rainfall_score, 2),
            },
            'risk_level': risk_level,
            'confidence': round(confidence, 2),
            'calculated_at': datetime.utcnow().isoformat(),
        }
    
    def _calculate_rainfall_risk(
        self,
        drought_score: float,
        latitude: float,
        longitude: float
    ) -> float:
        """
        Calculate rainfall risk (too much or too little)
        This is a simplified calculation - can be enhanced with actual rainfall data
        """
        # Inverse relationship with drought (more drought = less rainfall risk from excess)
        # But also consider flood risk from heavy rainfall
        base_rainfall_risk = 50.0  # Base risk
        
        # Adjust based on region (simplified)
        # In monsoon-heavy regions, excess rainfall is a risk
        if 20 <= latitude <= 30:  # Typical monsoon region
            excess_rainfall_risk = 40
        else:
            excess_rainfall_risk = 20
        
        # Combine drought (deficit) and excess risks
        rainfall_risk = (drought_score * 0.6) + (excess_rainfall_risk * 0.4)
        
        return min(100, max(0, rainfall_risk))
    
    def _determine_risk_level(self, score: float) -> str:
        """Determine risk level from score"""
        if score < 25:
            return "low"
        elif score < 50:
            return "moderate"
        elif score < 75:
            return "high"
        else:
            return "extreme"
    
    def _calculate_confidence(self, scores: list) -> float:
        """
        Calculate confidence based on model agreement
        Lower variance = higher confidence
        """
        if len(scores) == 0:
            return 0.0
        
        variance = np.var(scores)
        # Normalize variance to 0-1 scale (assuming max variance is 2500 for 0-100 range)
        normalized_variance = min(1.0, variance / 2500.0)
        confidence = 1.0 - normalized_variance
        
        return max(0.5, min(1.0, confidence))  # Clamp between 0.5 and 1.0
    
    def forecast(
        self,
        latitude: float,
        longitude: float,
        years: list,
        **kwargs
    ) -> Dict:
        """
        Generate future forecasts for specified years
        
        Args:
            latitude: Latitude
            longitude: Longitude
            years: List of years into the future
            **kwargs: Additional parameters
            
        Returns:
            Dictionary with forecasts for each year
        """
        forecasts = []
        current_score_data = self.calculate_score(latitude, longitude, **kwargs)
        current_score = current_score_data['clima_risk_score']
        
        for year in sorted(years):
            # Simple linear projection (can be enhanced with time-series models)
            # In reality, each model would have its own forecasting logic
            
            # Estimate future score with trend
            trend_factor = 1.0 + (year * 0.01)  # 1% increase per year (simplified)
            
            predicted_score = min(100, current_score * trend_factor)
            predicted_level = self._determine_risk_level(predicted_score)
            
            # Project individual risks
            breakdown = current_score_data['risk_breakdown']
            predicted_flood = min(100, breakdown['flood'] * trend_factor)
            predicted_heat = min(100, breakdown['heat'] * trend_factor * 1.05)  # Heat increases faster
            predicted_drought = min(100, breakdown['drought'] * trend_factor)
            predicted_groundwater = min(100, breakdown['groundwater'] * trend_factor * 1.03)
            predicted_rainfall = min(100, breakdown['rainfall'] * trend_factor)
            
            # Calculate confidence intervals (simplified)
            confidence_interval = predicted_score * 0.1  # ±10%
            
            forecasts.append({
                'year': year,
                'predicted_clima_risk_score': round(predicted_score, 2),
                'predicted_risk_level': predicted_level,
                'predicted_flood_risk': round(predicted_flood, 2),
                'predicted_heat_risk': round(predicted_heat, 2),
                'predicted_drought_risk': round(predicted_drought, 2),
                'predicted_groundwater_risk': round(predicted_groundwater, 2),
                'predicted_rainfall_risk': round(predicted_rainfall, 2),
                'confidence_interval_lower': round(predicted_score - confidence_interval, 2),
                'confidence_interval_upper': round(predicted_score + confidence_interval, 2),
            })
        
        return {
            'forecasts': forecasts,
            'current_score': current_score,
            'forecasted_at': datetime.utcnow().isoformat(),
        }

