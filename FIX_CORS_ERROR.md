# 🔧 Fix "Failed to Fetch" CORS Error

## ✅ Quick Fix - 3 Steps

### Step 1: Restart Backend with New CORS Settings

The backend code has been updated to allow all origins. **You need to restart it:**

1. **Find the terminal running the backend** (or stop any existing one)
2. **Press Ctrl+C** to stop it
3. **Start it again:**
   ```bash
   python -m uvicorn app.main:app --reload --port 8000
   ```

### Step 2: Use the UI Server (Avoids CORS Issues)

Instead of opening the HTML file directly, use the UI server:

```bash
python serve_ui.py
```

This will:
- ✅ Start a web server on http://localhost:3000
- ✅ Open the UI in your browser automatically
- ✅ Fix all CORS issues

### Step 3: Test It!

The UI should now work perfectly! Try:
1. Click "📍 Delhi" button
2. Click "Calculate Risk Score"
3. You should see results! 🎉

---

## Why This Happens

Browsers block requests from `file://` URLs to `localhost` for security (CORS policy).

**Solution:** Serve the HTML through an HTTP server (like `serve_ui.py` does)

---

## Alternative: Test Backend Directly

To verify the backend is working, test it directly:

```bash
curl http://localhost:8000/health
```

Or visit: http://localhost:8000/docs (API documentation)

---

## Summary

**To fix the error:**

1. ✅ Restart backend: `python -m uvicorn app.main:app --reload --port 8000`
2. ✅ Start UI server: `python serve_ui.py`
3. ✅ Use the UI at: http://localhost:3000

That's it! 🚀

