"""
Simple script to open the ClimaRisk AI UI in your browser
"""
import webbrowser
import os
from pathlib import Path

# Get the path to the HTML file
html_file = Path(__file__).parent / "frontend" / "index.html"
html_path = html_file.absolute()

print(f"\n{'='*60}")
print("ClimaRisk AI - Opening UI")
print(f"{'='*60}\n")
print(f"Opening: {html_path}")
print(f"\nMake sure the backend API is running on http://localhost:8000")
print(f"   If not, run: python -m uvicorn app.main:app --reload --port 8000\n")

# Open in default browser
webbrowser.open(f"file:///{html_path}")

print("UI opened in your browser!\n")
print("Tip: You can also open it manually by:")
print(f"   - Double-clicking: {html_file}\n")

