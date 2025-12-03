"""
API Router for v1 endpoints
"""
from fastapi import APIRouter

from app.api.v1.endpoints import score, forecast, risk_map, property as property_endpoint, bulk

api_router = APIRouter()

# Include all endpoint routers
api_router.include_router(score.router, prefix="/score", tags=["scoring"])
api_router.include_router(forecast.router, prefix="/forecast", tags=["forecasting"])
api_router.include_router(risk_map.router, prefix="/risk-map", tags=["maps"])
api_router.include_router(property_endpoint.router, prefix="/property", tags=["property"])
api_router.include_router(bulk.router, prefix="", tags=["bulk"])

