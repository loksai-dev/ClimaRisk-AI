# How to Run ClimaRisk AI

## Quick Start (Simplest Way)

### Option 1: Run API Only (No Database Required for Testing)

1. **Install minimal dependencies:**
```bash
pip install fastapi uvicorn pydantic pydantic-settings
```

2. **Run the server:**
```bash
python run_server.py
```

Or directly:
```bash
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

3. **Access the API:**
- API: http://localhost:8000
- Interactive Docs: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

4. **Test it:**
```bash
curl http://localhost:8000/health
```

Or visit http://localhost:8000/docs in your browser to test the API interactively!

### Option 2: Full Setup with Docker (Recommended)

1. **Make sure Docker Desktop is running**

2. **Start all services:**
```bash
docker-compose up -d
```

3. **Wait for services to be healthy (about 30 seconds)**

4. **Initialize database:**
```bash
docker-compose exec api alembic upgrade head
```

5. **Access:**
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- MinIO: http://localhost:9001

### Option 3: Local Development (Step by Step)

1. **Install Python 3.9+**

2. **Create virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac
```

3. **Install core dependencies:**
```bash
pip install fastapi uvicorn pydantic pydantic-settings numpy pandas
```

4. **Start the server:**
```bash
python run_server.py
```

5. **Test the API:**
Open http://localhost:8000/docs in your browser

## Testing the API

### Using the Interactive Docs (Easiest)

1. Go to http://localhost:8000/docs
2. Click on any endpoint (e.g., `POST /api/v1/score`)
3. Click "Try it out"
4. Enter test data:
```json
{
  "latitude": 28.6139,
  "longitude": 77.2090,
  "property_type": "residential"
}
```
5. Click "Execute"

### Using curl

```bash
# Health check
curl http://localhost:8000/health

# Get risk score
curl -X POST "http://localhost:8000/api/v1/score" ^
  -H "Content-Type: application/json" ^
  -d "{\"latitude\": 28.6139, \"longitude\": 77.2090, \"property_type\": \"residential\"}"
```

### Using Python

```python
import requests

# Test health
response = requests.get("http://localhost:8000/health")
print(response.json())

# Get risk score
response = requests.post(
    "http://localhost:8000/api/v1/score",
    json={
        "latitude": 28.6139,
        "longitude": 77.2090,
        "property_type": "residential"
    }
)
print(response.json())
```

## Troubleshooting

### Port 8000 already in use
- Change port: `uvicorn app.main:app --port 8001`
- Or stop the process using port 8000

### Module not found errors
- Install missing packages: `pip install <package-name>`
- Or install minimal requirements: `pip install fastapi uvicorn pydantic`

### Database connection errors (if using database)
- The API will still work for risk scoring without database
- Database is only needed for storing results

## What Works Without Database

✅ Risk scoring (`/api/v1/score`)  
✅ Forecasting (`/api/v1/forecast`)  
✅ Property analysis (`/api/v1/property/analysis`)  
✅ Bulk scoring (`/api/v1/bulk-scoring`)  

The ML models work entirely in memory - no database needed!

## Next Steps

1. **Explore the API**: Visit http://localhost:8000/docs
2. **Try different locations**: Test with coordinates from different cities
3. **Read the docs**: Check `README.md` and `docs/` folder
4. **Contribute**: See `CONTRIBUTING.md`

Happy testing! 🚀

