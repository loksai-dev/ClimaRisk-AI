# 🌍 ClimaRisk AI - Open-Source Climate Risk Prediction System

**Predict climate-related risks for any property in India & Asia using AI**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

## 📋 Problem Statement

Climate change is rapidly increasing the risk of floods, heatwaves, droughts, and groundwater depletion across India and Asia. However, home buyers, real-estate developers, banks, and insurance companies have no simple, reliable tool to understand how safe a piece of land or property will be in the next 10–30 years.

### Current Challenges:
- ❌ People unknowingly buy property in future high-risk zones
- ❌ Banks issue loans without climate-risk assessment
- ❌ Cities expand into environmentally unstable areas
- ❌ No consumer-friendly, India/Asia-focused climate risk tool exists
- ❌ Existing solutions are either US-only or enterprise-only
- ❌ No open-source platform for multi-risk climate prediction

## 🎯 Solution

**ClimaRisk AI** is a fully open-source platform that predicts long-term environmental risks for any land/property using:

- 📊 Historical weather data (IMD, NASA)
- 🛰️ Satellite climate patterns (ESA, MODIS)
- 🌡️ Heat island trends
- 💧 Rainfall & drought models
- 🌊 Flood probability maps
- 💾 Groundwater depletion data

### Key Features:

1. **ClimaRisk Score (0–100)** - Combined score for heat, flood, drought, groundwater, and rainfall risk
2. **Geospatial Risk Map** - Color-coded risk layers on Google Maps/OpenStreetMap
3. **Future Climate Forecast** - Predictive modeling for 5–30 years
4. **Open APIs** - For banks, insurance companies, real estate platforms, and government

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Frontend Layer                          │
│  React + Leaflet + OpenStreetMap + Mapbox GL                │
│  - Consumer Dashboard                                        │
│  - Bank/Enterprise Dashboard                                 │
│  - Risk Visualization                                        │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│                   API Gateway (FastAPI)                      │
│  /score, /forecast, /risk-map, /property/analysis, /bulk    │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              ML Inference Layer (Python)                     │
│  - Flood Risk Model                                          │
│  - Heat Wave Model                                           │
│  - Drought Model                                             │
│  - Groundwater Depletion Model                               │
│  - Ensemble Scoring Engine                                   │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Data Processing Layer                           │
│  - Apache Airflow / Prefect Pipelines                        │
│  - Data Ingestion (NASA, IMD, ESA, Government)              │
│  - Feature Engineering                                       │
│  - Geospatial Processing (PostGIS)                           │
└────────────────────┬────────────────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────────────────┐
│              Storage Layer                                   │
│  - PostgreSQL + PostGIS (Geospatial)                         │
│  - TimescaleDB (Time-series)                                 │
│  - Redis (Caching)                                           │
│  - MinIO/S3 (Object Storage)                                 │
└─────────────────────────────────────────────────────────────┘
```

## 🛠️ Tech Stack (100% Open-Source)

### Backend
- **FastAPI** - High-performance API framework
- **Python 3.9+** - Core language
- **PostgreSQL + PostGIS** - Geospatial database
- **TimescaleDB** - Time-series extension
- **Redis** - Caching layer
- **Apache Airflow / Prefect** - Data pipelines

### ML/AI
- **PyTorch / TensorFlow** - Deep learning
- **Scikit-learn** - Traditional ML
- **XGBoost** - Gradient boosting
- **Rasterio** - Geospatial raster processing
- **GeoPandas** - Geospatial data analysis
- **NumPy, Pandas** - Data processing

### Frontend
- **React 18+** - UI framework
- **Leaflet** - Interactive maps
- **OpenStreetMap** - Map tiles
- **Mapbox GL** - Advanced mapping
- **Chart.js / D3.js** - Data visualization
- **TypeScript** - Type safety

### Infrastructure
- **Docker** - Containerization
- **Kubernetes** - Orchestration
- **Nginx** - Reverse proxy
- **Celery** - Async task processing
- **MinIO** - S3-compatible object storage

## 📦 Installation

### Prerequisites
- Python 3.9+
- PostgreSQL 14+ with PostGIS extension
- Redis
- Docker & Docker Compose (optional)

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ClimaRiskAI.git
cd ClimaRiskAI
```

2. **Set up virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your database, API keys, etc.
```

5. **Set up database**
```bash
# Start PostgreSQL with PostGIS
docker-compose up -d postgres

# Run migrations
alembic upgrade head
```

6. **Run the application**
```bash
# Start backend
uvicorn app.main:app --reload

# Start frontend (in another terminal)
cd frontend
npm install
npm start
```

## 🚀 API Endpoints

### Core Endpoints

#### Get Climate Risk Score
```http
POST /api/v1/score
Content-Type: application/json

{
  "latitude": 28.6139,
  "longitude": 77.2090,
  "property_type": "residential"
}
```

Response:
```json
{
  "clima_risk_score": 45.2,
  "risk_breakdown": {
    "flood": 32.1,
    "heat": 58.5,
    "drought": 41.2,
    "groundwater": 52.8,
    "rainfall": 35.6
  },
  "risk_level": "moderate",
  "confidence": 0.87
}
```

#### Get Future Forecast
```http
POST /api/v1/forecast
Content-Type: application/json

{
  "latitude": 28.6139,
  "longitude": 77.2090,
  "years": [5, 10, 15, 20, 25, 30]
}
```

#### Get Risk Map
```http
GET /api/v1/risk-map?bbox=77.1,28.5,77.3,28.7&risk_type=flood
```

#### Property Analysis
```http
POST /api/v1/property/analysis
Content-Type: application/json

{
  "address": "Connaught Place, New Delhi",
  "property_details": {
    "type": "apartment",
    "floor": 3,
    "area_sqm": 120
  }
}
```

#### Bulk Scoring (for banks/enterprise)
```http
POST /api/v1/bulk-scoring
Content-Type: application/json

{
  "properties": [
    {"latitude": 28.6139, "longitude": 77.2090},
    {"latitude": 19.0760, "longitude": 72.8777}
  ]
}
```

## 📊 Data Sources

### Open-Source Datasets

1. **Weather Data**
   - IMD (India Meteorological Department) - Historical weather
   - NASA POWER - Global weather data
   - OpenWeatherMap API

2. **Satellite Data**
   - MODIS (NASA) - Land surface temperature
   - ESA Climate Change Initiative
   - Sentinel-2 - High-resolution imagery

3. **Flood Data**
   - Global Flood Database (Google)
   - India Water Resources Information System
   - Digital Elevation Models (SRTM)

4. **Groundwater Data**
   - Central Ground Water Board (CGWB) India
   - Global Groundwater Information System

5. **Drought Data**
   - Standardized Precipitation Index (SPI)
   - US Drought Monitor equivalent for Asia

## 🧪 ML Models

### Multi-Risk Ensemble Model

The system uses an ensemble of specialized models:

1. **Flood Risk Model**
   - Features: Elevation, proximity to rivers, historical flood events, rainfall patterns
   - Algorithm: XGBoost + CNN for spatial patterns

2. **Heat Wave Model**
   - Features: Urban heat island effect, historical temperatures, population density
   - Algorithm: LSTM for temporal patterns + Random Forest

3. **Drought Model**
   - Features: Precipitation patterns, soil moisture, vegetation indices
   - Algorithm: Gradient Boosting + Time-series analysis

4. **Groundwater Depletion Model**
   - Features: Historical groundwater levels, extraction rates, recharge patterns
   - Algorithm: Prophet (Facebook) for forecasting + Regression

5. **Ensemble Scorer**
   - Combines all models with weighted averaging
   - Adaptive weighting based on region-specific risk factors

## 📁 Project Structure

```
ClimaRiskAI/
├── app/                          # Backend application
│   ├── api/                     # API routes
│   │   ├── v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── score.py
│   │   │   │   ├── forecast.py
│   │   │   │   ├── risk_map.py
│   │   │   │   └── property.py
│   │   │   └── router.py
│   ├── core/                    # Core configuration
│   │   ├── config.py
│   │   └── security.py
│   ├── db/                      # Database
│   │   ├── models/
│   │   ├── schemas/
│   │   └── session.py
│   ├── ml/                      # ML models
│   │   ├── models/
│   │   │   ├── flood_model.py
│   │   │   ├── heat_model.py
│   │   │   ├── drought_model.py
│   │   │   └── groundwater_model.py
│   │   ├── ensemble.py
│   │   └── inference.py
│   ├── pipelines/               # Data pipelines
│   │   ├── ingestion/
│   │   ├── processing/
│   │   └── feature_engineering.py
│   └── main.py
├── frontend/                     # React frontend
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── App.tsx
│   └── package.json
├── notebooks/                    # Jupyter notebooks
│   ├── data_exploration/
│   ├── model_training/
│   └── evaluation/
├── data/                         # Data storage
│   ├── raw/
│   ├── processed/
│   └── models/
├── tests/                        # Tests
├── docker/                       # Docker configs
├── k8s/                          # Kubernetes configs
├── docs/                         # Documentation
├── requirements.txt
├── docker-compose.yml
└── README.md
```

## 🔐 Security

- API key authentication for enterprise users
- Rate limiting
- Input validation and sanitization
- HTTPS/TLS encryption
- SQL injection prevention (SQLAlchemy ORM)
- CORS configuration

## 🚢 Deployment

### Docker Compose
```bash
docker-compose up -d
```

### Kubernetes
```bash
kubectl apply -f k8s/
```

### Production Checklist
- [ ] Set up environment variables
- [ ] Configure database backups
- [ ] Set up monitoring (Prometheus + Grafana)
- [ ] Configure logging (ELK stack)
- [ ] Set up CI/CD pipeline
- [ ] Enable HTTPS/TLS
- [ ] Configure rate limiting
- [ ] Set up alerting

## 📈 Roadmap

### Phase 1: MVP (Months 1-2)
- [x] Core architecture setup
- [ ] Basic ML models
- [ ] API endpoints
- [ ] Simple frontend
- [ ] Data ingestion for 2-3 sources

### Phase 2: Enhancement (Months 3-4)
- [ ] Advanced ML models
- [ ] Full data pipeline
- [ ] Enhanced frontend
- [ ] Performance optimization
- [ ] Comprehensive testing

### Phase 3: Scale (Months 5-6)
- [ ] Multi-region support
- [ ] Enterprise features
- [ ] Advanced analytics
- [ ] Mobile app (optional)
- [ ] Community contributions

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- India Meteorological Department (IMD)
- NASA for satellite data
- ESA for climate datasets
- OpenStreetMap contributors
- All open-source contributors

## 📞 Contact

- **Project Lead**: [Your Name]
- **Email**: [your.email@example.com]
- **GitHub**: [@yourusername](https://github.com/yourusername)

---

**Built with ❤️ for a climate-resilient future**

