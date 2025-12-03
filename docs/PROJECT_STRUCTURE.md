# ClimaRisk AI - Project Structure

## Directory Tree

```
ClimaRiskAI/
│
├── 📁 app/                           # Main backend application
│   ├── __init__.py
│   ├── main.py                       # FastAPI application entry point
│   │
│   ├── 📁 api/                       # API layer
│   │   ├── __init__.py
│   │   └── 📁 v1/                    # API version 1
│   │       ├── __init__.py
│   │       ├── router.py             # Main API router
│   │       └── 📁 endpoints/         # API endpoints
│   │           ├── __init__.py
│   │           ├── score.py          # Risk scoring endpoint
│   │           ├── forecast.py       # Forecasting endpoint
│   │           ├── risk_map.py       # Risk map endpoint
│   │           ├── property.py       # Property analysis endpoint
│   │           └── bulk.py           # Bulk scoring endpoint
│   │
│   ├── 📁 core/                      # Core configuration
│   │   ├── __init__.py
│   │   ├── config.py                 # Application settings
│   │   ├── security.py               # Authentication/security
│   │   └── celery_app.py             # Celery configuration
│   │
│   ├── 📁 db/                        # Database layer
│   │   ├── __init__.py
│   │   ├── session.py                # Database session management
│   │   ├── 📁 models/                # SQLAlchemy models
│   │   │   ├── __init__.py
│   │   │   ├── property.py           # Property model
│   │   │   └── climate_data.py       # Climate data models
│   │   └── 📁 schemas/               # Pydantic schemas
│   │       ├── __init__.py
│   │       ├── score.py              # Score request/response schemas
│   │       ├── forecast.py           # Forecast schemas
│   │       └── property.py           # Property schemas
│   │
│   ├── 📁 ml/                        # Machine Learning
│   │   ├── __init__.py
│   │   ├── ensemble.py               # Ensemble scoring engine
│   │   └── 📁 models/                # Individual risk models
│   │       ├── __init__.py
│   │       ├── flood_model.py        # Flood risk model
│   │       ├── heat_model.py         # Heat risk model
│   │       ├── drought_model.py      # Drought risk model
│   │       └── groundwater_model.py  # Groundwater risk model
│   │
│   ├── 📁 pipelines/                 # Data processing pipelines
│   │   ├── __init__.py
│   │   ├── feature_engineering.py    # Feature engineering
│   │   └── 📁 ingestion/             # Data ingestion
│   │       ├── __init__.py
│   │       ├── nasa_ingestion.py     # NASA data ingestion
│   │       ├── imd_ingestion.py      # IMD data ingestion
│   │       └── groundwater_ingestion.py  # Groundwater data
│   │
│   └── 📁 tasks/                     # Celery tasks
│       └── __init__.py
│
├── 📁 frontend/                      # React frontend
│   ├── package.json                  # NPM dependencies
│   ├── vite.config.ts                # Vite configuration
│   ├── tsconfig.json                 # TypeScript config
│   ├── index.html                    # HTML entry point
│   └── 📁 src/                       # Source code
│       ├── main.tsx                  # React entry point
│       └── App.tsx                   # Main App component
│
├── 📁 docker/                        # Docker configurations
│   ├── Dockerfile.api                # Backend Dockerfile
│   ├── init-postgres.sql             # PostGIS initialization
│   └── nginx.conf                    # Nginx configuration
│
├── 📁 docs/                          # Documentation
│   ├── ARCHITECTURE.md               # System architecture
│   ├── ROADMAP.md                    # Development roadmap
│   └── PROJECT_STRUCTURE.md          # This file
│
├── 📁 tests/                         # Test suite
│   ├── __init__.py
│   ├── test_models.py                # ML model tests
│   ├── test_ensemble.py              # Ensemble tests
│   └── test_api.py                   # API endpoint tests
│
├── 📁 notebooks/                     # Jupyter notebooks
│   └── README.md                     # Notebooks documentation
│
├── 📁 data/                          # Data storage
│   ├── 📁 raw/                       # Raw data files
│   ├── 📁 processed/                 # Processed data
│   └── 📁 models/                    # Trained ML models
│
├── 📁 alembic/                       # Database migrations
│   ├── env.py                        # Alembic environment
│   └── script.py.mako                # Migration template
│
├── 📄 README.md                      # Main project README
├── 📄 QUICKSTART.md                  # Quick start guide
├── 📄 PROJECT_SUMMARY.md             # Project summary
├── 📄 CONTRIBUTING.md                # Contribution guidelines
├── 📄 LICENSE                        # MIT License
├── 📄 requirements.txt               # Python dependencies
├── 📄 docker-compose.yml             # Docker Compose configuration
├── 📄 alembic.ini                    # Alembic configuration
└── 📄 .gitignore                     # Git ignore rules
```

## Key Files Explained

### Backend Core

- **`app/main.py`**: FastAPI application initialization, middleware, routes
- **`app/core/config.py`**: All configuration settings (database, API keys, etc.)
- **`app/core/security.py`**: Authentication, password hashing, JWT tokens

### API Endpoints

- **`app/api/v1/endpoints/score.py`**: Calculate risk scores
- **`app/api/v1/endpoints/forecast.py`**: Get future forecasts
- **`app/api/v1/endpoints/risk_map.py`**: Generate risk map data
- **`app/api/v1/endpoints/property.py`**: Property analysis
- **`app/api/v1/endpoints/bulk.py`**: Bulk scoring for enterprise

### Database

- **`app/db/session.py`**: Database connection and session management
- **`app/db/models/`**: SQLAlchemy ORM models (Property, ClimateData, RiskScore, Forecast)
- **`app/db/schemas/`**: Pydantic schemas for API validation

### ML Models

- **`app/ml/ensemble.py`**: Combines all risk models into final score
- **`app/ml/models/flood_model.py`**: Flood risk prediction
- **`app/ml/models/heat_model.py`**: Heat wave risk prediction
- **`app/ml/models/drought_model.py`**: Drought risk prediction
- **`app/ml/models/groundwater_model.py`**: Groundwater depletion risk

### Data Pipelines

- **`app/pipelines/ingestion/`**: Fetch data from external sources (NASA, IMD, CGWB)
- **`app/pipelines/feature_engineering.py`**: Process raw data into ML features

### Infrastructure

- **`docker-compose.yml`**: Complete stack (PostgreSQL, Redis, MinIO, API, Workers)
- **`docker/Dockerfile.api`**: Backend container definition
- **`alembic/`**: Database migration management

## Code Organization Principles

### 1. Separation of Concerns
- **API Layer**: Request handling, validation, responses
- **Business Logic**: ML models, scoring algorithms
- **Data Layer**: Database models, schemas
- **Infrastructure**: Configuration, deployment

### 2. Modularity
- Each risk model is independent
- Data sources are separate modules
- Endpoints are organized by functionality

### 3. Scalability
- Stateless API design
- Async support (FastAPI)
- Task queue (Celery) for heavy operations
- Horizontal scaling ready

### 4. Maintainability
- Type hints throughout
- Comprehensive docstrings
- Clear naming conventions
- Organized directory structure

## Data Flow

```
API Request
    ↓
API Endpoint (validation)
    ↓
Business Logic / ML Models
    ↓
Database Query/Update
    ↓
Response
```

## Adding New Features

### New API Endpoint

1. Create endpoint file in `app/api/v1/endpoints/`
2. Add router to `app/api/v1/router.py`
3. Create schemas in `app/db/schemas/`
4. Write tests in `tests/`

### New Risk Model

1. Create model file in `app/ml/models/`
2. Implement `predict()` method
3. Add to ensemble scorer
4. Update tests

### New Data Source

1. Create ingestion module in `app/pipelines/ingestion/`
2. Add feature engineering if needed
3. Create pipeline in `app/pipelines/`
4. Schedule in Celery/Airflow

## Testing Structure

- **`tests/test_models.py`**: Unit tests for ML models
- **`tests/test_ensemble.py`**: Ensemble scoring tests
- **`tests/test_api.py`**: API endpoint integration tests

## Documentation Structure

- **`README.md`**: Project overview, installation, usage
- **`docs/ARCHITECTURE.md`**: Detailed system architecture
- **`docs/ROADMAP.md`**: Development roadmap
- **`QUICKSTART.md`**: Quick setup guide
- **`CONTRIBUTING.md`**: Contribution guidelines

## Configuration Files

- **`.env`**: Environment variables (not in git)
- **`requirements.txt`**: Python package dependencies
- **`docker-compose.yml`**: Service orchestration
- **`alembic.ini`**: Database migration config

---

This structure follows Python and web development best practices, making it easy to understand, maintain, and extend.

