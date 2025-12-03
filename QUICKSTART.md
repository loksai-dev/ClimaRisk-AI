# ClimaRisk AI - Quick Start Guide

Get ClimaRisk AI up and running in minutes!

## Prerequisites

- Docker & Docker Compose
- Python 3.9+ (if running locally)
- PostgreSQL 14+ with PostGIS (if not using Docker)

## Option 1: Docker Compose (Recommended)

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ClimaRiskAI.git
cd ClimaRiskAI
```

### 2. Configure environment

```bash
cp .env.example .env
# Edit .env with your settings (optional for local development)
```

### 3. Start services

```bash
docker-compose up -d
```

This will start:
- PostgreSQL with PostGIS
- Redis
- MinIO (object storage)
- FastAPI backend
- Celery workers

### 4. Initialize database

```bash
docker-compose exec api alembic upgrade head
```

### 5. Access the application

- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **MinIO Console**: http://localhost:9001 (minioadmin/minioadmin)

### 6. Test the API

```bash
curl -X POST "http://localhost:8000/api/v1/score" \
  -H "Content-Type: application/json" \
  -d '{
    "latitude": 28.6139,
    "longitude": 77.2090,
    "property_type": "residential"
  }'
```

## Option 2: Local Development

### 1. Install dependencies

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Set up database

Start PostgreSQL and create database:

```sql
CREATE DATABASE climarisk_db;
CREATE EXTENSION postgis;
```

Or use Docker:

```bash
docker run -d \
  --name climarisk_postgres \
  -e POSTGRES_DB=climarisk_db \
  -e POSTGRES_USER=climarisk \
  -e POSTGRES_PASSWORD=password \
  -p 5432:5432 \
  postgis/postgis:15-3.4
```

### 3. Configure environment

```bash
cp .env.example .env
# Edit .env with your database URL and settings
```

### 4. Run database migrations

```bash
alembic upgrade head
```

### 5. Start Redis (optional, for caching)

```bash
docker run -d --name redis -p 6379:6379 redis:7-alpine
```

### 6. Start the backend

```bash
uvicorn app.main:app --reload
```

### 7. Run tests

```bash
pytest
```

## Frontend Setup

### 1. Navigate to frontend directory

```bash
cd frontend
```

### 2. Install dependencies

```bash
npm install
```

### 3. Start development server

```bash
npm run dev
```

Frontend will be available at http://localhost:3000

## Common Commands

### Database

```bash
# Create new migration
alembic revision --autogenerate -m "Description"

# Apply migrations
alembic upgrade head

# Rollback migration
alembic downgrade -1
```

### Docker

```bash
# View logs
docker-compose logs -f api

# Restart services
docker-compose restart

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test
pytest tests/test_models.py
```

## Next Steps

1. **Explore the API**: Visit http://localhost:8000/docs
2. **Read Documentation**: Check `docs/ARCHITECTURE.md` and `docs/ROADMAP.md`
3. **Contribute**: See `CONTRIBUTING.md`
4. **Train Models**: Check `notebooks/` directory

## Troubleshooting

### Database connection errors

- Check PostgreSQL is running
- Verify DATABASE_URL in .env
- Ensure PostGIS extension is installed

### Port already in use

- Change ports in docker-compose.yml
- Or stop the service using the port

### Import errors

- Ensure virtual environment is activated
- Reinstall requirements: `pip install -r requirements.txt`

### Docker issues

- Check Docker is running
- Review logs: `docker-compose logs`
- Try rebuilding: `docker-compose build --no-cache`

## Support

- **Issues**: https://github.com/yourusername/ClimaRiskAI/issues
- **Documentation**: See `docs/` directory
- **Questions**: Open a GitHub discussion

Happy coding! 🚀

