# How to Run the UI (Fix CORS Issues)

## The Problem

Opening `index.html` directly from file system (file://) causes CORS (Cross-Origin) errors because browsers block requests from file:// to localhost.

## Solution: Use the UI Server

I've created a simple HTTP server to serve the UI properly.

### Step 1: Start the Backend API

**Terminal 1:**
```bash
python -m uvicorn app.main:app --reload --port 8000
```

### Step 2: Start the UI Server

**Terminal 2:**
```bash
python serve_ui.py
```

This will:
- Start a web server on http://localhost:3000
- Serve the UI files properly
- Open the UI in your browser automatically

### Step 3: Use the UI

The UI will open at: **http://localhost:3000**

Now it should work perfectly! ✅

---

## Alternative: Direct File Access (Quick Test)

If you just want to test quickly:

1. **Update CORS** (already done in code):
   - The backend now allows all origins (`allow_origins=["*"]`)
   - But you still need to restart the backend for changes to take effect

2. **Restart the backend**:
   - Stop the current server (Ctrl+C)
   - Start again: `python -m uvicorn app.main:app --reload --port 8000`

3. **Open HTML file**:
   - Double-click `frontend/index.html`
   - May still have CORS issues in some browsers

**Recommended: Use `serve_ui.py` for best results!**

---

## Quick Start (All in One)

**Terminal 1 - Backend:**
```bash
python -m uvicorn app.main:app --reload --port 8000
```

**Terminal 2 - UI Server:**
```bash
python serve_ui.py
```

That's it! The UI will open automatically. 🚀

