from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pathlib import Path
import os

# Get the backend directory
BACKEND_DIR = Path(__file__).parent.parent
DATABASE_PATH = BACKEND_DIR / "database.db"

# Use absolute path for database (Windows compatible)
# Convert to string and replace backslashes for SQLite
db_path_str = str(DATABASE_PATH.absolute()).replace("\\", "/")
DATABASE_URL = f"sqlite:///{db_path_str}"

# Export DATABASE_PATH for use in scripts
__all__ = ['engine', 'SessionLocal', 'Base', 'DATABASE_PATH', 'DATABASE_URL']

# Create engine with proper configuration
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False},
    echo=False  # Set to True for SQL query logging
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
