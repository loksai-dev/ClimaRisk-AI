# ClimaRisk AI - UI Guide

## ✅ Complete UI is Ready!

The complete frontend UI has been created and opened in your browser!

## 🚀 How to Use

### 1. Make Sure Backend is Running

The UI needs the backend API to be running. If it's not running:

```bash
python -m uvicorn app.main:app --reload --port 8000
```

### 2. Open the UI

**Option A: Use the script**
```bash
python open_ui.py
```

**Option B: Open manually**
- Navigate to: `frontend/index.html`
- Double-click to open in your browser

### 3. Features Available

✅ **Location Input**
- Enter latitude/longitude manually
- Or click quick location buttons (Delhi, Mumbai, Bangalore, Chennai)
- Or click on the map to select a location

✅ **Risk Score Calculation**
- Click "Calculate Risk Score" button
- Get comprehensive risk analysis with:
  - Overall ClimaRisk Score (0-100)
  - Individual risk breakdowns (Flood, Heat, Drought, Groundwater, Rainfall)
  - Risk level classification (Low, Moderate, High, Extreme)
  - Personalized recommendations

✅ **Future Forecast**
- Click "Get Forecast (5-30 years)" button
- See risk predictions for 5, 10, 15, 20, 25, and 30 years
- Interactive chart showing risk trends over time

✅ **Interactive Map**
- Click anywhere on the map to select coordinates
- Marker shows selected location
- Map updates automatically when you enter coordinates

## 📊 Understanding the Results

### Risk Score
- **0-25**: Low Risk ✅
- **25-50**: Moderate Risk ⚠️
- **50-75**: High Risk 🔴
- **75-100**: Extreme Risk ⛔

### Risk Breakdown
Each risk type is scored 0-100:
- **Flood**: Risk of flooding events
- **Heat**: Heat wave and extreme temperature risk
- **Drought**: Water scarcity and drought risk
- **Groundwater**: Groundwater depletion risk
- **Rainfall**: Rainfall variability risk

## 🎯 Quick Test

1. **Use a Quick Location**: Click "📍 Delhi" button
2. **Calculate Risk**: Click "Calculate Risk Score"
3. **View Results**: See the comprehensive risk analysis
4. **Get Forecast**: Click "Get Forecast" to see future predictions

## 🔧 Troubleshooting

### API Not Connected
- Check if backend is running: http://localhost:8000/health
- The status is shown at the bottom of the page
- Start backend with: `python -m uvicorn app.main:app --reload --port 8000`

### Map Not Loading
- Check your internet connection (map tiles load from OpenStreetMap)
- Wait a few seconds for tiles to load

### No Results
- Make sure coordinates are valid:
  - Latitude: -90 to 90
  - Longitude: -180 to 180
- Check browser console for errors (F12)

## 📁 File Structure

```
frontend/
  └── index.html    # Complete UI (single file, no dependencies needed!)
```

The UI is completely self-contained - just one HTML file with everything included!

## 🎨 Features

- ✨ Modern, responsive design
- 🗺️ Interactive map with OpenStreetMap
- 📊 Beautiful charts with Chart.js
- 📱 Mobile-friendly
- 🎯 Easy to use
- ⚡ Fast and lightweight

## 🌟 Next Steps

1. Try different locations across India and Asia
2. Compare risk scores between cities
3. View long-term forecasts for your area
4. Share with others!

Enjoy using ClimaRisk AI! 🚀

