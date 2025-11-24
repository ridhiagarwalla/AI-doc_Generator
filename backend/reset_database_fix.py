"""
Reset and recreate database with correct schema
This will DELETE all existing data and recreate tables
"""
import sys
import os
from pathlib import Path

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, Base, DATABASE_PATH
from app.models import User, Project, Content, Refinement
from sqlalchemy import inspect

def reset_database():
    """Drop all tables and recreate them with correct schema"""
    print("=" * 60)
    print("🔄 Resetting Database...")
    print("=" * 60)
    
    try:
        # Drop all tables
        print("\n1. Dropping all existing tables...")
        Base.metadata.drop_all(bind=engine)
        print("   ✅ All tables dropped")
        
        # Create all tables with correct schema
        print("\n2. Creating tables with correct schema...")
        Base.metadata.create_all(bind=engine)
        print("   ✅ All tables created")
        
        # Verify tables
        print("\n3. Verifying tables...")
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        required_tables = ["users", "projects", "content", "refinements"]
        
        for table in required_tables:
            if table in tables:
                print(f"   ✅ Table '{table}' exists")
                # Check columns
                columns = [col['name'] for col in inspector.get_columns(table)]
                print(f"      Columns: {', '.join(columns)}")
            else:
                print(f"   ❌ Table '{table}' missing!")
                return False
        
        print("\n" + "=" * 60)
        print("✅ Database reset successfully!")
        print("✅ All tables created with correct schema")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"\n❌ Error resetting database: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("\n⚠️  WARNING: This will DELETE all existing data!")
    response = input("Are you sure you want to continue? (yes/no): ")
    
    if response.lower() in ['yes', 'y']:
        success = reset_database()
        sys.exit(0 if success else 1)
    else:
        print("❌ Operation cancelled.")
        sys.exit(0)

