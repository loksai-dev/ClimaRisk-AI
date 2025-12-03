"""
NASA Data Ingestion Pipeline
Fetches data from NASA POWER (Prediction Of Worldwide Energy Resources) API
and other NASA climate datasets
"""
import requests
import pandas as pd
from typing import Dict, List, Optional
from datetime import datetime, timedelta
import time


class NASADataIngestion:
    """
    Ingest climate data from NASA APIs
    
    Data sources:
    - NASA POWER API: Weather and climate data
    - MODIS: Land surface temperature
    - Other NASA Earth observation datasets
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize NASA data ingestion"""
        self.api_key = api_key
        self.power_base_url = "https://power.larc.nasa.gov/api/temporal/daily/point"
    
    def fetch_weather_data(
        self,
        latitude: float,
        longitude: float,
        start_date: str,
        end_date: str,
        parameters: Optional[List[str]] = None
    ) -> Dict:
        """
        Fetch weather data from NASA POWER API
        
        Args:
            latitude: Latitude
            longitude: Longitude
            start_date: Start date (YYYYMMDD)
            end_date: End date (YYYYMMDD)
            parameters: List of parameters to fetch
            
        Returns:
            Dictionary with weather data
        """
        if parameters is None:
            parameters = [
                "T2M",  # Temperature at 2m
                "T2M_MAX",  # Maximum temperature
                "T2M_MIN",  # Minimum temperature
                "PRECTOTCORR",  # Precipitation
                "RH2M",  # Relative humidity
            ]
        
        try:
            params = {
                "parameters": ",".join(parameters),
                "community": "RE",
                "longitude": longitude,
                "latitude": latitude,
                "start": start_date,
                "end": end_date,
                "format": "JSON",
            }
            
            response = requests.get(self.power_base_url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            
            # Process and format data
            processed_data = self._process_power_data(data, latitude, longitude)
            
            return processed_data
        
        except requests.exceptions.RequestException as e:
            print(f"Error fetching NASA POWER data: {str(e)}")
            return {}
    
    def _process_power_data(self, data: Dict, latitude: float, longitude: float) -> Dict:
        """Process raw NASA POWER API response"""
        processed = {
            'latitude': latitude,
            'longitude': longitude,
            'data_source': 'NASA_POWER',
            'records': []
        }
        
        if 'properties' not in data:
            return processed
        
        properties = data['properties']
        parameter_keys = [k for k in properties.keys() if k != 'parameter']
        
        # Get dates from first parameter
        if parameter_keys:
            first_param = parameter_keys[0]
            dates = properties[first_param]
            
            for i, date_str in enumerate(dates):
                record = {
                    'date': date_str,
                    'latitude': latitude,
                    'longitude': longitude,
                }
                
                # Extract all parameter values for this date
                for param_key in parameter_keys:
                    param_name = param_key.replace(' ', '_').lower()
                    if i < len(properties[param_key]):
                        record[param_name] = properties[param_key][i]
                
                processed['records'].append(record)
        
        return processed
    
    def fetch_modis_temperature(
        self,
        latitude: float,
        longitude: float,
        start_date: str,
        end_date: str
    ) -> Dict:
        """
        Fetch MODIS land surface temperature data
        
        Note: This is a placeholder. In production, would use:
        - MODIS API or cloud storage
        - Google Earth Engine
        - AWS Earth Observation datasets
        """
        # Placeholder - would implement actual MODIS data fetching
        return {
            'latitude': latitude,
            'longitude': longitude,
            'data_source': 'MODIS',
            'start_date': start_date,
            'end_date': end_date,
            'records': []
        }
    
    def batch_fetch_for_region(
        self,
        bbox: tuple,  # (min_lon, min_lat, max_lon, max_lat)
        start_date: str,
        end_date: str,
        grid_spacing: float = 0.5  # Degrees
    ) -> List[Dict]:
        """
        Fetch data for multiple points in a region
        
        Args:
            bbox: Bounding box (min_lon, min_lat, max_lon, max_lat)
            start_date: Start date
            end_date: End date
            grid_spacing: Grid spacing in degrees
            
        Returns:
            List of data dictionaries
        """
        min_lon, min_lat, max_lon, max_lat = bbox
        
        all_data = []
        
        # Generate grid points
        lat = min_lat
        while lat <= max_lat:
            lon = min_lon
            while lon <= max_lon:
                data = self.fetch_weather_data(
                    latitude=lat,
                    longitude=lon,
                    start_date=start_date,
                    end_date=end_date
                )
                
                if data.get('records'):
                    all_data.append(data)
                
                # Rate limiting
                time.sleep(0.1)
                
                lon += grid_spacing
            lat += grid_spacing
        
        return all_data

