"""
Start both backend API and UI server
"""
import subprocess
import sys
import time
import webbrowser
from pathlib import Path

def start_backend():
    """Start the backend API server"""
    print("Starting backend API server...")
    backend_process = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--reload", "--port", "8000"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return backend_process

def start_ui():
    """Start the UI server"""
    print("Starting UI server...")
    ui_script = Path(__file__).parent / "serve_ui.py"
    ui_process = subprocess.Popen(
        [sys.executable, str(ui_script)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return ui_process

def main():
    print(f"\n{'='*60}")
    print("ClimaRisk AI - Starting All Services")
    print(f"{'='*60}\n")
    
    print("Starting services in separate windows...\n")
    print("Terminal windows will open for:")
    print("  1. Backend API (port 8000)")
    print("  2. UI Server (port 3000)\n")
    print(f"{'='*60}\n")
    
    # Start backend in new window
    backend_cmd = f'start cmd /k "python -m uvicorn app.main:app --reload --port 8000"'
    subprocess.Popen(backend_cmd, shell=True)
    
    time.sleep(2)  # Wait a bit for backend to start
    
    # Start UI in new window
    ui_cmd = f'start cmd /k "python serve_ui.py"'
    subprocess.Popen(ui_cmd, shell=True)
    
    print("✅ Services started in separate windows!")
    print("\nWait a few seconds for services to start, then:")
    print("  - Backend: http://localhost:8000")
    print("  - UI: http://localhost:3000")
    print("\nThe UI should open automatically in your browser.\n")

if __name__ == "__main__":
    main()

