@echo off
echo Stopping any existing backend servers...
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *uvicorn*" 2>nul
timeout /t 2 /nobreak >nul
echo.
echo Starting backend API server...
python -m uvicorn app.main:app --reload --port 8000
pause

