# ClimaRisk AI - System Architecture

## Overview

ClimaRisk AI is a comprehensive, open-source climate risk prediction system designed specifically for India and Asia. The system uses multiple data sources and machine learning models to predict long-term environmental risks for properties and land.

## System Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │   Web UI     │  │  Mobile App  │  │  API Clients │        │
│  │  (React)     │  │   (Future)   │  │  (Banks/     │        │
│  └──────┬───────┘  └──────┬───────┘  │   Insurance) │        │
│         │                  │          └──────┬───────┘        │
└─────────┼──────────────────┼──────────────────┼───────────────┘
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    API GATEWAY LAYER                            │
│  ┌─────────────────────────────────────────────────────────┐  │
│  │              FastAPI Application                        │  │
│  │  • Authentication & Authorization                       │  │
│  │  • Rate Limiting                                        │  │
│  │  • Request Validation                                   │  │
│  │  • CORS Handling                                        │  │
│  └───────────────────────┬─────────────────────────────────┘  │
└──────────────────────────┼──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    APPLICATION LAYER                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │  API Routes  │  │  Business    │  │  Data        │        │
│  │  • /score    │  │  Logic       │  │  Processing  │        │
│  │  • /forecast │  │  Services    │  │  Services    │        │
│  │  • /risk-map │  │              │  │              │        │
│  │  • /property │  │              │  │              │        │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘        │
└─────────┼──────────────────┼──────────────────┼───────────────┘
          │                  │                  │
┌─────────▼──────────────────▼──────────────────▼───────────────┐
│                    ML INFERENCE LAYER                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   Ensemble   │  │   Flood      │  │   Heat       │       │
│  │   Scorer     │  │   Model      │  │   Model      │       │
│  └──────┬───────┘  └──────────────┘  └──────────────┘       │
│         │                                                    │
│  ┌──────▼───────┐  ┌──────────────┐                        │
│  │   Drought    │  │ Groundwater  │                        │
│  │   Model      │  │   Model      │                        │
│  └──────────────┘  └──────────────┘                        │
└──────────────────────────────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    DATA PROCESSING LAYER                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │   Data       │  │   Feature    │  │   Data       │        │
│  │ Ingestion    │  │ Engineering  │  │  Cleaning    │        │
│  │ Pipelines    │  │              │  │              │        │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘        │
│         │                  │                  │                 │
│  ┌──────▼──────────────────▼──────────────────▼────────────┐  │
│  │         Apache Airflow / Prefect Workflows              │  │
│  │  • Scheduled data ingestion                             │  │
│  │  • ETL processes                                        │  │
│  │  • Model retraining                                     │  │
│  └─────────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                      STORAGE LAYER                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │ PostgreSQL   │  │   Redis      │  │   MinIO/S3   │        │
│  │ + PostGIS    │  │   Cache      │  │   Object     │        │
│  │ + Timescale  │  │              │  │   Storage    │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└────────────────────────────────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────────────┐
│                    EXTERNAL DATA SOURCES                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │    NASA      │  │     IMD      │  │     ESA      │        │
│  │   POWER API  │  │   Weather    │  │   Climate    │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        │
│  │    CGWB      │  │  Government  │  │  OpenStreet  │        │
│  │ Groundwater  │  │  Datasets    │  │     Map      │        │
│  └──────────────┘  └──────────────┘  └──────────────┘        │
└────────────────────────────────────────────────────────────────┘
```

## Component Details

### 1. API Gateway (FastAPI)

**Responsibilities:**
- Request routing and validation
- Authentication and authorization
- Rate limiting
- CORS handling
- Request/response logging

**Key Endpoints:**
- `POST /api/v1/score` - Calculate risk score
- `POST /api/v1/forecast` - Get future forecasts
- `GET /api/v1/risk-map` - Get risk map data
- `POST /api/v1/property/analysis` - Comprehensive property analysis
- `POST /api/v1/bulk-scoring` - Bulk scoring for enterprise

### 2. ML Inference Layer

**Ensemble Scorer:**
- Combines predictions from multiple risk models
- Weighted averaging based on region and risk type
- Confidence calculation based on model agreement

**Individual Models:**
- **Flood Risk Model**: Elevation, proximity to water, historical floods
- **Heat Risk Model**: Urban heat island, historical temperatures
- **Drought Model**: Precipitation patterns, SPI, soil moisture
- **Groundwater Model**: Historical levels, extraction rates, recharge

### 3. Data Processing Layer

**Data Ingestion:**
- NASA POWER API integration
- IMD weather data ingestion
- CGWB groundwater data
- ESA satellite data
- Government datasets

**Feature Engineering:**
- Temporal aggregations
- Statistical features
- Anomaly detection
- Geospatial features

**Pipelines:**
- Scheduled data updates
- ETL processes
- Data quality checks
- Model feature generation

### 4. Storage Layer

**PostgreSQL + PostGIS:**
- Property data with geospatial indexing
- Climate data (time-series)
- Risk scores and forecasts
- User and API key management

**Redis:**
- API response caching
- Session management
- Rate limiting counters

**MinIO/S3:**
- Large datasets
- Model artifacts
- Raster/imagery data

## Data Flow

### Risk Score Calculation Flow

1. **Request Received**: API receives location (lat/lon) and property details
2. **Feature Extraction**: System fetches/calculates features:
   - Historical climate data
   - Elevation (DEM)
   - Proximity features
   - Regional characteristics
3. **Model Inference**: Each risk model generates a score:
   - Flood model → flood_risk (0-100)
   - Heat model → heat_risk (0-100)
   - Drought model → drought_risk (0-100)
   - Groundwater model → groundwater_risk (0-100)
4. **Ensemble Scoring**: Ensemble combines scores with weights:
   - Weighted average
   - Risk level classification
   - Confidence calculation
5. **Response**: Return comprehensive score with breakdown

### Forecast Generation Flow

1. **Request**: Location and forecast years
2. **Current Score**: Calculate current risk score
3. **Trend Analysis**: Analyze historical trends for each risk type
4. **Projection**: Apply time-series models (Prophet, LSTM) to project future
5. **Uncertainty**: Calculate confidence intervals
6. **Response**: Return forecasts for each requested year

## Scalability Considerations

### Horizontal Scaling
- Stateless API servers (can scale horizontally)
- Load balancer (Nginx) for request distribution
- Redis for shared caching and rate limiting

### Database Scaling
- Read replicas for PostgreSQL
- Partitioning for time-series data (TimescaleDB)
- Connection pooling

### ML Model Serving
- Model caching in memory
- Batch processing for bulk requests
- Async processing for heavy computations

### Data Pipeline Scaling
- Distributed task queue (Celery)
- Parallel processing of data ingestion
- Incremental updates instead of full refreshes

## Security

- **Authentication**: JWT tokens for API access
- **Authorization**: Role-based access control
- **Rate Limiting**: Per-user/IP limits
- **Input Validation**: Pydantic schemas
- **SQL Injection**: SQLAlchemy ORM protection
- **CORS**: Configurable allowed origins
- **HTTPS**: TLS encryption (production)

## Monitoring & Observability

- **Logging**: Structured logging (Structlog)
- **Metrics**: Prometheus metrics
- **Tracing**: Request tracing for debugging
- **Health Checks**: `/health` endpoint
- **Error Tracking**: Centralized error logging

## Deployment Architecture

### Development
- Docker Compose for local development
- All services in containers
- Local data storage

### Production
- Kubernetes orchestration
- Managed databases (RDS/Cloud SQL)
- Object storage (S3/GCS)
- CDN for static assets
- Auto-scaling based on load

## Performance Optimization

- **Caching**: Redis caching for frequent queries
- **Database Indexing**: Geospatial indexes, time-series optimizations
- **Lazy Loading**: Load models only when needed
- **Batch Processing**: Bulk operations for enterprise
- **CDN**: Static asset delivery

## Future Enhancements

- Real-time risk alerts
- Mobile applications
- Advanced visualization (3D maps)
- More data sources
- Improved ML models (deep learning)
- Regional model fine-tuning
- Collaborative filtering for similar properties

