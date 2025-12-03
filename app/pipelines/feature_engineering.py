"""
Feature Engineering for Climate Risk Models
Processes raw data into features for ML models
"""
import pandas as pd
import numpy as np
from typing import Dict, List, Optional
from datetime import datetime, timedelta


class FeatureEngineer:
    """
    Engineered features for climate risk prediction
    
    Creates features like:
    - Temporal aggregations (monthly, seasonal, annual)
    - Trends and anomalies
    - Statistical features
    - Geospatial features
    """
    
    def __init__(self):
        """Initialize feature engineer"""
        pass
    
    def process_weather_features(
        self,
        weather_data: pd.DataFrame,
        latitude: float,
        longitude: float
    ) -> Dict:
        """
        Process raw weather data into features
        
        Args:
            weather_data: DataFrame with weather records
            latitude: Latitude
            longitude: Longitude
            
        Returns:
            Dictionary of engineered features
        """
        features = {
            'latitude': latitude,
            'longitude': longitude,
            'temporal_features': {},
            'statistical_features': {},
            'anomaly_features': {},
        }
        
        if weather_data.empty:
            return features
        
        # Ensure date column is datetime
        if 'date' in weather_data.columns:
            weather_data['date'] = pd.to_datetime(weather_data['date'])
            weather_data = weather_data.sort_values('date')
        
        # Temperature features
        if 'temperature_avg' in weather_data.columns:
            temp_col = 'temperature_avg'
            
            # Statistical features
            features['statistical_features']['temp_mean'] = weather_data[temp_col].mean()
            features['statistical_features']['temp_std'] = weather_data[temp_col].std()
            features['statistical_features']['temp_max'] = weather_data[temp_col].max()
            features['statistical_features']['temp_min'] = weather_data[temp_col].min()
            
            # Trend features
            if len(weather_data) > 1:
                features['statistical_features']['temp_trend'] = self._calculate_trend(
                    weather_data[temp_col].values
                )
            
            # Seasonal features
            if 'date' in weather_data.columns:
                weather_data['month'] = weather_data['date'].dt.month
                features['temporal_features']['temp_seasonal_amplitude'] = (
                    weather_data.groupby('month')[temp_col].mean().std()
                )
        
        # Precipitation features
        if 'precipitation' in weather_data.columns:
            prec_col = 'precipitation'
            
            features['statistical_features']['prec_total'] = weather_data[prec_col].sum()
            features['statistical_features']['prec_mean'] = weather_data[prec_col].mean()
            features['statistical_features']['prec_max'] = weather_data[prec_col].max()
            features['statistical_features']['dry_days'] = (weather_data[prec_col] < 1).sum()
            features['statistical_features']['wet_days'] = (weather_data[prec_col] >= 1).sum()
            
            # Drought indicators
            if len(weather_data) >= 30:  # At least monthly data
                monthly_prec = weather_data.groupby(
                    weather_data['date'].dt.to_period('M')
                )[prec_col].sum()
                features['statistical_features']['prec_cv'] = monthly_prec.std() / monthly_prec.mean()
        
        # Anomaly detection
        features['anomaly_features'] = self._detect_anomalies(weather_data)
        
        return features
    
    def _calculate_trend(self, values: np.ndarray) -> float:
        """Calculate linear trend (slope)"""
        if len(values) < 2:
            return 0.0
        
        x = np.arange(len(values))
        slope = np.polyfit(x, values, 1)[0]
        return slope
    
    def _detect_anomalies(self, data: pd.DataFrame) -> Dict:
        """Detect anomalies in climate data"""
        anomalies = {}
        
        # Temperature anomalies
        if 'temperature_avg' in data.columns:
            temp_mean = data['temperature_avg'].mean()
            temp_std = data['temperature_avg'].std()
            
            if temp_std > 0:
                anomalies['temp_anomaly_count'] = (
                    (data['temperature_avg'] > temp_mean + 2 * temp_std) |
                    (data['temperature_avg'] < temp_mean - 2 * temp_std)
                ).sum()
                anomalies['temp_extreme_events'] = (
                    data['temperature_avg'] > temp_mean + 3 * temp_std
                ).sum()
        
        # Precipitation anomalies
        if 'precipitation' in data.columns:
            prec_mean = data['precipitation'].mean()
            prec_std = data['precipitation'].std()
            
            if prec_std > 0:
                anomalies['prec_anomaly_count'] = (
                    data['precipitation'] > prec_mean + 2 * prec_std
                ).sum()
        
        return anomalies
    
    def create_geospatial_features(
        self,
        latitude: float,
        longitude: float,
        elevation: Optional[float] = None
    ) -> Dict:
        """
        Create geospatial features
        
        Args:
            latitude: Latitude
            longitude: Longitude
            elevation: Elevation in meters (optional)
            
        Returns:
            Dictionary of geospatial features
        """
        features = {
            'latitude': latitude,
            'longitude': longitude,
            'elevation': elevation,
            'region_features': {},
        }
        
        # Climate zone classification
        features['region_features']['climate_zone'] = self._classify_climate_zone(latitude)
        
        # Monsoon region
        features['region_features']['monsoon_region'] = self._is_monsoon_region(
            latitude, longitude
        )
        
        # Coastal proximity (simplified)
        features['region_features']['coastal'] = self._is_coastal(latitude, longitude)
        
        return features
    
    def _classify_climate_zone(self, latitude: float) -> str:
        """Classify climate zone based on latitude"""
        if latitude < 23.5:
            return 'tropical'
        elif latitude < 30:
            return 'subtropical'
        else:
            return 'temperate'
    
    def _is_monsoon_region(self, latitude: float, longitude: float) -> bool:
        """Check if location is in monsoon region"""
        # Simplified check
        return 20 <= latitude <= 30 and 70 <= longitude <= 95
    
    def _is_coastal(self, latitude: float, longitude: float) -> bool:
        """Check if location is coastal"""
        # Very simplified
        coastal_ranges = [
            (8, 23, 68, 72),  # West coast
            (19, 23, 80, 97),  # East coast
        ]
        
        for min_lat, max_lat, min_lon, max_lon in coastal_ranges:
            if min_lat <= latitude <= max_lat and min_lon <= longitude <= max_lon:
                return True
        
        return False

