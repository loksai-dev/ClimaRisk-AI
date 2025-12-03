"""
Quick script to check if the server is running
"""
import requests
import sys

try:
    # Check health endpoint
    response = requests.get("http://localhost:8000/health", timeout=2)
    if response.status_code == 200:
        print("\n" + "="*50)
        print("✅ SERVER IS RUNNING!")
        print("="*50)
        print(f"\nStatus: {response.status_code}")
        print(f"Response: {response.json()}")
        print("\n📍 URLs:")
        print("  • API Documentation: http://localhost:8000/docs")
        print("  • Health Check: http://localhost:8000/health")
        print("  • Root: http://localhost:8000/")
        print("\n🎯 Next Steps:")
        print("  1. Open http://localhost:8000/docs in your browser")
        print("  2. Try the API endpoints interactively!")
        print("="*50 + "\n")
        sys.exit(0)
    else:
        print(f"⚠️  Server responded with status {response.status_code}")
        sys.exit(1)
except requests.exceptions.ConnectionError:
    print("\n" + "="*50)
    print("❌ Server is NOT running")
    print("="*50)
    print("\nTo start the server, run:")
    print("  python -m uvicorn app.main:app --reload --port 8000")
    print("\nOr:")
    print("  python run_server.py")
    print("="*50 + "\n")
    sys.exit(1)
except Exception as e:
    print(f"\n❌ Error checking server: {e}")
    sys.exit(1)

