"""
Groundwater Depletion Risk Model
Predicts groundwater depletion risk based on historical levels, extraction rates, etc.
"""
import numpy as np
from typing import Optional


class GroundwaterRiskModel:
    """
    Groundwater depletion risk prediction model
    
    Features considered:
    - Historical groundwater levels
    - Extraction rates
    - Recharge potential
    - Aquifer characteristics
    - Agricultural intensity
    """
    
    def __init__(self):
        """Initialize groundwater risk model"""
        self.model_loaded = False
    
    def predict(
        self,
        latitude: float,
        longitude: float,
        current_water_level: Optional[float] = None,
        **kwargs
    ) -> float:
        """
        Predict groundwater risk score (0-100)
        
        Args:
            latitude: Latitude
            longitude: Longitude
            current_water_level: Current groundwater level in meters (optional)
            **kwargs: Additional features
            
        Returns:
            Groundwater risk score (0-100)
        """
        base_risk = 40.0
        
        # Region-based risk (known critical zones)
        regional_risk = self._get_regional_groundwater_risk(latitude, longitude)
        
        # Agricultural intensity (higher agriculture = higher extraction)
        agricultural_intensity = self._estimate_agricultural_intensity(latitude, longitude)
        
        # Recharge potential (based on precipitation and geology)
        recharge_potential = self._estimate_recharge_potential(latitude, longitude)
        
        # Combine factors
        groundwater_risk = (
            regional_risk * 0.5 +
            agricultural_intensity * 0.3 +
            (100 - recharge_potential) * 0.2  # Lower recharge = higher risk
        )
        
        return min(100, max(0, groundwater_risk))
    
    def _get_regional_groundwater_risk(self, latitude: float, longitude: float) -> float:
        """
        Get risk based on known critical groundwater zones in India
        Based on CGWB (Central Ground Water Board) data
        """
        # Critical zones (simplified based on known problem areas)
        # Punjab-Haryana region (very high extraction)
        if 29 <= latitude <= 31 and 74 <= longitude <= 77:
            return 85
        
        # Northwestern regions (Rajasthan, Gujarat)
        elif 24 <= latitude <= 29 and 70 <= longitude <= 76:
            return 75
        
        # Central India (Madhya Pradesh, parts of Maharashtra)
        elif 22 <= latitude <= 26 and 74 <= longitude <= 80:
            return 65
        
        # Tamil Nadu (some critical blocks)
        elif 10 <= latitude <= 13 and 76 <= longitude <= 80:
            return 60
        
        # Northeastern regions (generally better)
        elif 24 <= latitude <= 30 and 88 <= longitude <= 97:
            return 35
        
        # Default moderate risk
        else:
            return 50
    
    def _estimate_agricultural_intensity(self, latitude: float, longitude: float) -> float:
        """Estimate agricultural intensity (higher = more groundwater extraction)"""
        # Known agricultural intensive regions
        # Punjab, Haryana (wheat-rice intensive)
        if 29 <= latitude <= 31 and 74 <= longitude <= 77:
            return 90
        
        # Western UP
        elif 26 <= latitude <= 29 and 77 <= longitude <= 81:
            return 75
        
        # Central India agricultural regions
        elif 22 <= latitude <= 26 and 75 <= longitude <= 82:
            return 65
        
        # Urban areas (lower agricultural intensity)
        elif self._is_likely_urban(latitude, longitude):
            return 30
        
        # Default moderate
        else:
            return 50
    
    def _estimate_recharge_potential(self, latitude: float, longitude: float) -> float:
        """Estimate groundwater recharge potential (higher = better)"""
        # Recharge depends on precipitation and geological conditions
        
        # High precipitation regions = higher recharge
        if 24 <= latitude <= 30 and 88 <= longitude <= 97:  # Northeastern
            return 80
        
        elif latitude < 18:  # Southern (varies)
            return 70
        
        # Low precipitation regions = lower recharge
        elif 23 <= latitude <= 30 and 68 <= longitude <= 76:  # Western arid
            return 30
        
        # Moderate
        else:
            return 55
    
    def _is_likely_urban(self, latitude: float, longitude: float) -> bool:
        """Check if location is likely urban"""
        major_cities = [
            (28.6139, 77.2090),  # Delhi
            (19.0760, 72.8777),  # Mumbai
            (13.0827, 80.2707),  # Chennai
            (12.9716, 77.5946),  # Bangalore
        ]
        
        for city_lat, city_lon in major_cities:
            distance = np.sqrt(
                (latitude - city_lat) ** 2 + (longitude - city_lon) ** 2
            )
            if distance < 0.5:
                return True
        
        return False
    
    def load_model(self, model_path: str):
        """Load trained model from file"""
        self.model_loaded = True

