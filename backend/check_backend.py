"""
Comprehensive Backend Health Check
Run this to verify everything is working correctly
"""
import sys
import os
from pathlib import Path

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def check_imports():
    """Check if all required modules can be imported"""
    print("🔍 Checking imports...")
    try:
        from app.database import engine, Base, SessionLocal
        from app.models import User, Project, Content, Refinement
        from app.schemas import UserCreate, UserLogin
        from app.auth.routes import router as auth_router
        from app.auth.utils import hash_password, verify_password
        from app.config import SECRET_KEY, ALGORITHM
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import error: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_database():
    """Check database connection and tables"""
    print("\n🔍 Checking database...")
    try:
        from app.database import engine, Base, SessionLocal
        from app.models import User, Project, Content, Refinement
        
        # Check if database file exists
        db_path = Path(__file__).parent / "database.db"
        if db_path.exists():
            print(f"✅ Database file exists: {db_path}")
        else:
            print(f"⚠️  Database file not found: {db_path}")
            print("   Run: python init_database.py")
        
        # Try to connect
        with engine.connect() as conn:
            print("✅ Database connection successful")
        
        # Check tables
        from sqlalchemy import inspect
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        required_tables = ["users", "projects", "content", "refinements"]
        
        for table in required_tables:
            if table in tables:
                print(f"✅ Table '{table}' exists")
            else:
                print(f"❌ Table '{table}' missing")
                return False
        
        return True
    except Exception as e:
        print(f"❌ Database error: {e}")
        import traceback
        traceback.print_exc()
        return False

def check_config():
    """Check configuration"""
    print("\n🔍 Checking configuration...")
    try:
        from app.config import SECRET_KEY, ALGORITHM, GEMINI_API_KEY
        
        if SECRET_KEY:
            print(f"✅ SECRET_KEY configured (length: {len(SECRET_KEY)})")
        else:
            print("⚠️  SECRET_KEY not set (using default)")
        
        if ALGORITHM:
            print(f"✅ ALGORITHM: {ALGORITHM}")
        
        if GEMINI_API_KEY:
            print("✅ GEMINI_API_KEY configured")
        else:
            print("⚠️  GEMINI_API_KEY not set (AI features will not work)")
        
        return True
    except Exception as e:
        print(f"❌ Config error: {e}")
        return False

def check_password_hashing():
    """Test password hashing"""
    print("\n🔍 Testing password hashing...")
    try:
        from app.auth.utils import hash_password, verify_password
        
        test_password = "test123"
        hashed = hash_password(test_password)
        
        if verify_password(test_password, hashed):
            print("✅ Password hashing works correctly")
            return True
        else:
            print("❌ Password verification failed")
            return False
    except Exception as e:
        print(f"❌ Password hashing error: {e}")
        return False

def main():
    """Run all checks"""
    print("=" * 60)
    print("🔧 Backend Health Check")
    print("=" * 60)
    
    results = []
    results.append(("Imports", check_imports()))
    results.append(("Database", check_database()))
    results.append(("Configuration", check_config()))
    results.append(("Password Hashing", check_password_hashing()))
    
    print("\n" + "=" * 60)
    print("📊 Summary")
    print("=" * 60)
    
    for name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {name}")
    
    all_passed = all(result for _, result in results)
    
    if all_passed:
        print("\n✅ All checks passed! Backend is ready.")
    else:
        print("\n❌ Some checks failed. Please fix the issues above.")
        print("\n💡 Common fixes:")
        print("   - Run: python init_database.py")
        print("   - Check: .env file exists in backend/")
        print("   - Install: pip install -r requirements.txt")
    
    return all_passed

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

