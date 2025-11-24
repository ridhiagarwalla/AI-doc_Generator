"""
Initialize database and create all tables
Run this script once to set up the database
"""
from .database import engine, Base
from .models import User, Project, Content, Refinement

def init_db():
    """Create all database tables"""
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

if __name__ == "__main__":
    init_db()

