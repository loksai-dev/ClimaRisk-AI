"""
Property model for storing property information
"""
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from geoalchemy2 import Geometry
import uuid

from app.db.session import Base


class Property(Base):
    """Property model"""
    __tablename__ = "properties"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    
    # Location
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String, nullable=True)
    city = Column(String, nullable=True)
    state = Column(String, nullable=True)
    country = Column(String, default="India")
    
    # Geospatial point
    location = Column(
        Geometry('POINT', srid=4326),
        nullable=False
    )
    
    # Property details
    property_type = Column(String)  # residential, commercial, industrial, agricultural
    area_sqm = Column(Float, nullable=True)
    floor = Column(Integer, nullable=True)
    
    # Metadata
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Additional metadata
    metadata = Column(JSON, nullable=True)
    
    # Indexes
    __table_args__ = (
        Index('idx_property_location', 'location', postgresql_using='gist'),
        Index('idx_property_lat_lon', 'latitude', 'longitude'),
    )

