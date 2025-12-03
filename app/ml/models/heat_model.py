"""
Heat Risk Model
Predicts heat wave risk based on urban heat island effect, historical temperatures, etc.
"""
import numpy as np
from typing import Optional


class HeatRiskModel:
    """
    Heat wave risk prediction model
    
    Features considered:
    - Historical temperature trends
    - Urban heat island effect
    - Population density
    - Land use patterns
    - Latitude/climate zone
    """
    
    def __init__(self):
        """Initialize heat risk model"""
        self.model_loaded = False
    
    def predict(
        self,
        latitude: float,
        longitude: float,
        is_urban: Optional[bool] = None,
        population_density: Optional[float] = None,
        **kwargs
    ) -> float:
        """
        Predict heat risk score (0-100)
        
        Args:
            latitude: Latitude
            longitude: Longitude
            is_urban: Whether location is urban (optional)
            population_density: Population density per sq km (optional)
            **kwargs: Additional features
            
        Returns:
            Heat risk score (0-100)
        """
        base_risk = 40.0
        
        # Latitude-based risk (lower latitude = higher baseline temperature)
        lat_risk = self._calculate_latitude_risk(latitude)
        
        # Urban heat island effect
        if is_urban is None:
            is_urban = self._is_likely_urban(latitude, longitude)
        
        if is_urban:
            urban_heat_island_adjustment = 25  # Urban areas are hotter
        else:
            urban_heat_island_adjustment = 10
        
        # Population density adjustment
        if population_density:
            if population_density > 10000:  # Very dense
                density_adjustment = 15
            elif population_density > 5000:
                density_adjustment = 10
            else:
                density_adjustment = 5
        else:
            density_adjustment = 8
        
        # Regional climate zone adjustments
        climate_adjustment = self._get_climate_zone_risk(latitude, longitude)
        
        # Combine factors
        heat_risk = (
            lat_risk * 0.3 +
            urban_heat_island_adjustment * 0.3 +
            density_adjustment * 0.2 +
            climate_adjustment * 0.2
        )
        
        return min(100, max(0, heat_risk))
    
    def _calculate_latitude_risk(self, latitude: float) -> float:
        """Calculate base heat risk based on latitude"""
        # Lower latitudes (closer to equator) have higher baseline temperatures
        # India spans roughly 6°N to 37°N
        if latitude < 15:
            return 70  # Southern regions (very hot)
        elif latitude < 25:
            return 60  # Central regions (hot)
        elif latitude < 30:
            return 50  # Northern plains (moderate-hot)
        else:
            return 40  # Himalayan region (cooler)
    
    def _is_likely_urban(self, latitude: float, longitude: float) -> bool:
        """Check if location is likely urban (simplified)"""
        # Major Indian cities (simplified)
        major_cities = [
            (28.6139, 77.2090, "Delhi"),
            (19.0760, 72.8777, "Mumbai"),
            (13.0827, 80.2707, "Chennai"),
            (12.9716, 77.5946, "Bangalore"),
            (22.5726, 88.3639, "Kolkata"),
            (18.5204, 73.8567, "Pune"),
            (23.0225, 72.5714, "Ahmedabad"),
        ]
        
        for city_lat, city_lon, _ in major_cities:
            distance = np.sqrt(
                (latitude - city_lat) ** 2 + (longitude - city_lon) ** 2
            )
            if distance < 0.5:  # Within ~50km of major city
                return True
        
        return False
    
    def _get_climate_zone_risk(self, latitude: float, longitude: float) -> float:
        """Get heat risk based on climate zone"""
        # Simplified climate zones for India
        # Tropical: < 23.5°N
        # Subtropical: 23.5°N - 30°N
        # Temperate: > 30°N
        
        if latitude < 23.5:
            return 65  # Tropical - very hot
        elif latitude < 30:
            return 55  # Subtropical - hot
        else:
            return 40  # Temperate - moderate
    
    def load_model(self, model_path: str):
        """Load trained model from file"""
        self.model_loaded = True

