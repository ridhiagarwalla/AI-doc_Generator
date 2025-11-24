import os
from pathlib import Path
from dotenv import load_dotenv

# Get the backend directory (parent of app directory)
BACKEND_DIR = Path(__file__).parent.parent
ENV_FILE = BACKEND_DIR / ".env"

# Load .env file from backend directory
if ENV_FILE.exists():
    load_dotenv(dotenv_path=ENV_FILE)
else:
    # Try loading from current directory as fallback
    load_dotenv()

# OpenRouter API Key (replaces Gemini)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
# Keep GEMINI_API_KEY for backward compatibility (deprecated)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Support both JWT_SECRET and SECRET_KEY for compatibility
SECRET_KEY = os.getenv("JWT_SECRET") or os.getenv("SECRET_KEY", "9a93535b8efd8813b0b819116cc827ea8c00ebed43caef498dfcece7895533b7")
ALGORITHM = os.getenv("JWT_ALGO", "HS256")
