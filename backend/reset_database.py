"""
Reset database - Use this if you have authentication issues or schema errors
WARNING: This will delete all data!
"""
import os
import sys
from pathlib import Path
from sqlalchemy import inspect

# Add backend to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.database import engine, Base, DATABASE_PATH
from app.models import User, Project, Content, Refinement

def reset_db():
    """Drop all tables and recreate them with correct schema"""
    print("=" * 60)
    print("🔄 Resetting Database...")
    print("=" * 60)
    print("⚠️  WARNING: This will delete all data!")
    response = input("Are you sure you want to reset the database? (yes/no): ")
    
    if response.lower() not in ["yes", "y"]:
        print("❌ Operation cancelled.")
        return
    
    try:
        # Drop all tables
        print("\n1. Dropping all existing tables...")
        Base.metadata.drop_all(bind=engine)
        print("   ✅ All tables dropped")
        
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
            print("✅ Database reset successfully!")
            print("✅ All tables recreated with correct schema")
            print("📝 You can now register a new account.")
            print("=" * 60)
        else:
            print("\n❌ Some tables are missing!")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Error resetting database: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    reset_db()

