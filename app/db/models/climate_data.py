"""
Climate data models
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid

from app.db.session import Base


class ClimateData(Base):
    """Historical climate data storage"""
    __tablename__ = "climate_data"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Location reference (can be property_id or lat/lon grid)
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.id"), nullable=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    
    # Time
    date = Column(DateTime(timezone=True), nullable=False)
    
    # Climate metrics
    temperature_avg = Column(Float, nullable=True)
    temperature_max = Column(Float, nullable=True)
    temperature_min = Column(Float, nullable=True)
    precipitation = Column(Float, nullable=True)
    humidity = Column(Float, nullable=True)
    
    # Additional metrics
    data_source = Column(String)  # IMD, NASA, ESA, etc.
    raw_data = Column(JSON, nullable=True)
    
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Indexes
    __table_args__ = (
        Index('idx_climate_location', 'latitude', 'longitude'),
        Index('idx_climate_date', 'date'),
        Index('idx_climate_property', 'property_id'),
    )


class RiskScore(Base):
    """Climate risk scores for properties"""
    __tablename__ = "risk_scores"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Property reference
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.id"), nullable=False)
    
    # Overall score
    clima_risk_score = Column(Float, nullable=False)  # 0-100
    risk_level = Column(String)  # low, moderate, high, extreme
    
    # Individual risk scores
    flood_risk = Column(Float, nullable=False)  # 0-100
    heat_risk = Column(Float, nullable=False)  # 0-100
    drought_risk = Column(Float, nullable=False)  # 0-100
    groundwater_risk = Column(Float, nullable=False)  # 0-100
    rainfall_risk = Column(Float, nullable=False)  # 0-100
    
    # Confidence and metadata
    confidence = Column(Float, default=1.0)  # 0-1
    model_version = Column(String, nullable=True)
    
    # Timestamp
    calculated_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Additional details
    details = Column(JSON, nullable=True)
    
    # Relationship
    property = relationship("Property", backref="risk_scores")
    
    # Indexes
    __table_args__ = (
        Index('idx_risk_score_property', 'property_id'),
        Index('idx_risk_score_calculated', 'calculated_at'),
    )


class Forecast(Base):
    """Future climate risk forecasts"""
    __tablename__ = "forecasts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Property reference
    property_id = Column(UUID(as_uuid=True), ForeignKey("properties.id"), nullable=False)
    
    # Forecast horizon
    forecast_year = Column(Integer, nullable=False)  # Years from now (5, 10, 15, etc.)
    
    # Forecasted scores
    predicted_clima_risk_score = Column(Float, nullable=False)
    predicted_risk_level = Column(String)
    
    # Individual predictions
    predicted_flood_risk = Column(Float)
    predicted_heat_risk = Column(Float)
    predicted_drought_risk = Column(Float)
    predicted_groundwater_risk = Column(Float)
    predicted_rainfall_risk = Column(Float)
    
    # Uncertainty metrics
    confidence_interval_lower = Column(Float, nullable=True)
    confidence_interval_upper = Column(Float, nullable=True)
    
    # Metadata
    model_version = Column(String)
    forecasted_at = Column(DateTime(timezone=True), server_default=func.now())
    details = Column(JSON, nullable=True)
    
    # Relationship
    property = relationship("Property", backref="forecasts")
    
    # Indexes
    __table_args__ = (
        Index('idx_forecast_property', 'property_id'),
        Index('idx_forecast_year', 'forecast_year'),
    )

