"""
Start server script - Use this to start the server without reload issues
"""
import uvicorn
import sys
import os
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

if __name__ == "__main__":
    # Check if .env exists
    env_file = backend_dir / ".env"
    if not env_file.exists():
        print("⚠️  Warning: .env file not found!")
        print("📝 Please create backend/.env with:")
        print("   JWT_SECRET=your-secret-key")
        print("   GEMINI_API_KEY=your-gemini-api-key")
        print("   DATABASE_URL=sqlite:///./database.db")
        print()
    
    # Check if database exists, if not initialize
    db_file = backend_dir / "database.db"
    if not db_file.exists():
        print("📝 Database not found. Initializing...")
        try:
            from app.init_db import init_db
            init_db()
        except Exception as e:
            print(f"⚠️  Could not initialize database: {e}")
            print("💡 Run: python init_database.py")
    
    print("🚀 Starting server...")
    print("📡 Backend will be available at: http://localhost:8000")
    print("📚 API docs will be available at: http://localhost:8000/docs")
    print("🛑 Press CTRL+C to stop")
    print()
    
    # Start server with reload disabled to prevent reload loops
    # Use --reload only in development if needed
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False,  # Disable reload to prevent loops
        log_level="info"
    )

