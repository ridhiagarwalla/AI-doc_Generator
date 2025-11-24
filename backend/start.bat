@echo off
REM Backend Startup Script for Windows

echo 🚀 Starting AI Document Generator Backend...

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -r requirements.txt

REM Check if .env file exists
if not exist ".env" (
    echo ⚠️  Warning: .env file not found!
    echo 📝 Please create a .env file with the following variables:
    echo    JWT_SECRET=your-secret-key
    echo    GEMINI_API_KEY=your-gemini-api-key
    echo    DATABASE_URL=sqlite:///./database.db
    pause
    exit /b 1
)

REM Initialize database
echo 🗄️  Initializing database...
python init_database.py

REM Start server
echo ✅ Starting FastAPI server...
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

pause

