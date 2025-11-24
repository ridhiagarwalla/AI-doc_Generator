"""
Check if everything is set up correctly
Run this to verify your setup before starting the server
"""
import sys
import os
from pathlib import Path

def check_setup():
    """Check all setup requirements"""
    print("🔍 Checking setup...")
    print()
    
    errors = []
    warnings = []
    
    # Check Python version
    print("1. Checking Python version...")
    if sys.version_info < (3, 8):
        errors.append(f"Python 3.8+ required. Current: {sys.version}")
        print(f"   ❌ Python version too old: {sys.version}")
    else:
        print(f"   ✅ Python version OK: {sys.version.split()[0]}")
    
    # Check .env file
    print("\n2. Checking .env file...")
    backend_dir = Path(__file__).parent
    env_file = backend_dir / ".env"
    if not env_file.exists():
        warnings.append(".env file not found in backend directory")
        print("   ⚠️  .env file not found!")
        print("   📝 Create backend/.env with:")
        print("      JWT_SECRET=your-secret-key")
        print("      GEMINI_API_KEY=your-gemini-api-key")
        print("      DATABASE_URL=sqlite:///./database.db")
    else:
        print("   ✅ .env file found")
        # Check if it has required variables
        with open(env_file, 'r') as f:
            content = f.read()
            if "GEMINI_API_KEY" not in content or "your-gemini-api-key" in content:
                warnings.append("GEMINI_API_KEY may not be set correctly")
                print("   ⚠️  GEMINI_API_KEY may need to be set")
            if "JWT_SECRET" not in content or "your-secret-key" in content:
                warnings.append("JWT_SECRET may not be set correctly")
                print("   ⚠️  JWT_SECRET may need to be set")
    
    # Check database
    print("\n3. Checking database...")
    db_file = backend_dir / "database.db"
    if db_file.exists():
        print("   ✅ Database file exists")
    else:
        warnings.append("Database not initialized")
        print("   ⚠️  Database not found. Run: python init_database.py")
    
    # Check imports
    print("\n4. Checking imports...")
    try:
        sys.path.insert(0, str(backend_dir))
        from app.database import engine, Base
        from app.models import User, Project, Content, Refinement
        from app.config import SECRET_KEY, ALGORITHM, GEMINI_API_KEY
        from app.auth.routes import router
        print("   ✅ All imports successful")
    except ImportError as e:
        errors.append(f"Import error: {e}")
        print(f"   ❌ Import error: {e}")
        print("   💡 Run: pip install -r requirements.txt")
    
    # Check dependencies
    print("\n5. Checking dependencies...")
    required_packages = [
        "fastapi", "uvicorn", "sqlalchemy", "python-jose", 
        "passlib", "python-dotenv", "google-generativeai",
        "python-docx", "python-pptx"
    ]
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing.append(package)
    
    if missing:
        errors.append(f"Missing packages: {', '.join(missing)}")
        print(f"   ❌ Missing packages: {', '.join(missing)}")
        print("   💡 Run: pip install -r requirements.txt")
    else:
        print("   ✅ All dependencies installed")
    
    # Summary
    print("\n" + "="*50)
    if errors:
        print("❌ ERRORS FOUND:")
        for error in errors:
            print(f"   - {error}")
        print("\n⚠️  Please fix these errors before running the server.")
        return False
    elif warnings:
        print("⚠️  WARNINGS:")
        for warning in warnings:
            print(f"   - {warning}")
        print("\n✅ Setup is mostly OK, but check warnings above.")
        return True
    else:
        print("✅ ALL CHECKS PASSED!")
        print("✅ Your setup is ready to go!")
        return True

if __name__ == "__main__":
    success = check_setup()
    sys.exit(0 if success else 1)

