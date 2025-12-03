# 🚀 ClimaRisk AI - Start Here!

## ✅ What's Been Built

You now have a complete **ClimaRisk AI** project with:
- ✅ Full backend API (FastAPI)
- ✅ 4 ML risk models (Flood, Heat, Drought, Groundwater)
- ✅ 5 API endpoints ready to use
- ✅ Complete project structure
- ✅ Documentation

## 🎯 Quick Start (Choose One)

### Option 1: Run API Immediately (No Database Needed)

The API can run **without a database** for testing the risk models!

1. **Open a terminal in the project folder**

2. **Install just what's needed:**
```bash
pip install fastapi uvicorn pydantic pydantic-settings numpy pandas
```

3. **Run the server:**
```bash
python run_server.py
```

Or:
```bash
python -m uvicorn app.main:app --reload --port 8000
```

4. **Open your browser:**
   - Go to: **http://localhost:8000/docs**
   - This opens the interactive API documentation
   - Click on any endpoint and try it out!

### Option 2: Use Docker (Full Stack)

If you have Docker installed:

```bash
docker-compose up -d
```

Wait 30 seconds, then:
- API: http://localhost:8000/docs
- All services will be running

## 📝 Testing the API

### Easiest Way: Interactive Docs

1. Start the server (Option 1 above)
2. Go to **http://localhost:8000/docs**
3. Click on `POST /api/v1/score`
4. Click "Try it out"
5. Enter this test data:
```json
{
  "latitude": 28.6139,
  "longitude": 77.2090,
  "property_type": "residential"
}
```
6. Click "Execute"
7. See the risk score!

### Test Different Locations

Try these coordinates:

**Delhi (High Risk)**
```json
{"latitude": 28.6139, "longitude": 77.2090}
```

**Mumbai (Coastal)**
```json
{"latitude": 19.0760, "longitude": 72.8777}
```

**Bangalore**
```json
{"latitude": 12.9716, "longitude": 77.5946}
```

## 🔍 Available Endpoints

1. **`GET /health`** - Check if server is running
2. **`POST /api/v1/score`** - Get climate risk score
3. **`POST /api/v1/forecast`** - Get future forecasts
4. **`POST /api/v1/property/analysis`** - Comprehensive property analysis
5. **`POST /api/v1/bulk-scoring`** - Score multiple properties

## 📚 What You Can Do Now

### 1. Test the Risk Models
- The ML models work **right now** - no training needed
- They use rule-based logic based on location
- Test different coordinates to see risk variations

### 2. Explore the Code
- **`app/ml/models/`** - Risk prediction models
- **`app/api/v1/endpoints/`** - API endpoints
- **`app/ml/ensemble.py`** - Combines all risks

### 3. Read the Docs
- **`README.md`** - Full project overview
- **`RUN.md`** - Detailed running instructions
- **`docs/ARCHITECTURE.md`** - System design
- **`docs/ROADMAP.md`** - Development plan

## 🛠️ Troubleshooting

### "Module not found" errors
Install missing packages:
```bash
pip install <package-name>
```

### Port 8000 in use
Use a different port:
```bash
python -m uvicorn app.main:app --port 8001
```

### Want to see what's happening?
The server shows logs in the terminal. Watch for:
- ✅ `Application startup complete`
- ✅ `Uvicorn running on http://0.0.0.0:8000`

## 🎉 Next Steps

1. **✅ Start the server** - Use Option 1 above
2. **✅ Test the API** - Visit http://localhost:8000/docs
3. **✅ Try different locations** - Test the risk models
4. **✅ Read the code** - Explore how it works
5. **✅ Customize** - Add your own features!

## 💡 Pro Tips

- The API works **without database** for testing
- Database is only needed to **store results**
- All ML models run **in memory**
- Interactive docs at `/docs` are your best friend!

## 📞 Need Help?

- Check **`RUN.md`** for detailed instructions
- See **`QUICKSTART.md`** for step-by-step guide
- Read **`docs/`** folder for architecture details

---

**Ready to go?** Run the server and visit http://localhost:8000/docs! 🚀

