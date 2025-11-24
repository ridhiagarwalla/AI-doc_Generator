"""
Test backend connection and imports
Run this to check for errors
"""
import sys
import os
from pathlib import Path

# Add backend to path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

print("=" * 60)
print("Testing Backend Connection")
print("=" * 60)

# Test 1: Check imports
print("\n1. Testing imports...")
try:
    from app.database import engine, Base, SessionLocal
    print("   ✅ Database imports OK")
except Exception as e:
    print(f"   ❌ Database import error: {e}")
    sys.exit(1)

try:
    from app.models import User, Project, Content, Refinement
    print("   ✅ Model imports OK")
except Exception as e:
    print(f"   ❌ Model import error: {e}")
    sys.exit(1)

try:
    from app.auth.routes import router as auth_router
    print("   ✅ Auth router imports OK")
except Exception as e:
    print(f"   ❌ Auth router import error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

try:
    from app.projects_routes import router as projects_router
    print("   ✅ Projects router imports OK")
except Exception as e:
    print(f"   ❌ Projects router import error: {e}")
    sys.exit(1)

try:
    from app.document_routes import router as document_router
    print("   ✅ Document router imports OK")
except Exception as e:
    print(f"   ❌ Document router import error: {e}")
    sys.exit(1)

try:
    from app.main import app
    print("   ✅ Main app imports OK")
except Exception as e:
    print(f"   ❌ Main app import error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

# Test 2: Check database connection
print("\n2. Testing database connection...")
try:
    from sqlalchemy import text
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    print("   ✅ Database connection OK")
except Exception as e:
    print(f"   ❌ Database connection error: {e}")
    sys.exit(1)

# Test 3: Check database tables
print("\n3. Testing database tables...")
try:
    Base.metadata.create_all(bind=engine)
    print("   ✅ Database tables OK")
except Exception as e:
    print(f"   ❌ Database table error: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("✅ All tests passed! Backend is ready.")
print("=" * 60)

