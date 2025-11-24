"""
Initialize database and create all tables
Run this script from the backend directory: python init_database.py
"""
import sys
import os
from pathlib import Path

# Add the backend directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, Base, DATABASE_PATH
from app.models import User, Project, Content, Refinement
from sqlalchemy import inspect

def init_db():
    """Create all database tables with correct schema"""
    print("=" * 60)
    print("🗄️  Initializing Database...")
    print("=" * 60)
    
    try:
        # Drop existing tables if they exist (to fix schema issues)
        print("\n1. Checking existing tables...")
        inspector = inspect(engine)
        existing_tables = inspector.get_table_names()
        
        if existing_tables:
            print(f"   ⚠️  Found {len(existing_tables)} existing table(s)")
            print("   Dropping existing tables to fix schema...")
            Base.metadata.drop_all(bind=engine)
            print("   ✅ Existing tables dropped")
        
        # Create all tables with correct schema
        print("\n2. Creating tables with correct schema...")
        Base.metadata.create_all(bind=engine)
        print("   ✅ All tables created")
        
        # Verify tables and columns
        print("\n3. Verifying schema...")
        inspector = inspect(engine)
        tables = inspector.get_table_names()
        required_tables = ["users", "projects", "content", "refinements"]
        
        all_ok = True
        for table in required_tables:
            if table in tables:
                columns = [col['name'] for col in inspector.get_columns(table)]
                print(f"   ✅ Table '{table}' - Columns: {', '.join(columns)}")
            else:
                print(f"   ❌ Table '{table}' missing!")
                all_ok = False
        
        if all_ok:
            print("\n" + "=" * 60)
            print("✅ Database initialized successfully!")
            print("✅ All tables created with correct schema")
            print("=" * 60)
        else:
            print("\n❌ Some tables are missing!")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Error initializing database: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    init_db()

