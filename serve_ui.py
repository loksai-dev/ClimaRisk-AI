"""
Simple HTTP server to serve the UI and avoid CORS issues
"""
import http.server
import socketserver
import webbrowser
from pathlib import Path
import os

PORT = 3000
UI_DIR = Path(__file__).parent / "frontend"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(UI_DIR), **kwargs)
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

def main():
    # Change to UI directory
    os.chdir(UI_DIR)
    
    print(f"\n{'='*60}")
    print("ClimaRisk AI - Starting UI Server")
    print(f"{'='*60}\n")
    print(f"UI Server: http://localhost:{PORT}")
    print(f"Backend API: http://localhost:8000")
    print(f"\nMake sure the backend is running!")
    print(f"   Run: python -m uvicorn app.main:app --reload --port 8000\n")
    print(f"Opening browser...\n")
    print(f"Press Ctrl+C to stop the server\n")
    print(f"{'='*60}\n")
    
    # Open browser
    webbrowser.open(f"http://localhost:{PORT}")
    
    # Start server
    with socketserver.TCPServer(("", PORT), CustomHTTPRequestHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print(f"\n\nServer stopped.")

if __name__ == "__main__":
    main()

