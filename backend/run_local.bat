@echo off
REM Simple startup script for local development - NO RELOAD

echo ========================================
echo   AI Document Generator - Backend
echo ========================================
echo.

REM Check if venv exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate venv
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Check .env
if not exist ".env" (
    echo.
    echo WARNING: .env file not found!
    echo Creating .env file...
    (
        echo JWT_SECRET=my-secret-key-change-this-12345
        echo JWT_ALGO=HS256
        echo GEMINI_API_KEY=your-gemini-api-key-here
        echo DATABASE_URL=sqlite:///./database.db
    ) > .env
    echo .env file created. Please update with your actual values.
    echo.
)

REM Initialize database if needed
if not exist "database.db" (
    echo Initializing database...
    python init_database.py
    echo.
)

REM Start server WITHOUT reload to prevent loops
echo Starting server (NO RELOAD)...
echo Server will be at: http://localhost:8000
echo API docs at: http://localhost:8000/docs
echo.
echo Press CTRL+C to stop
echo.

uvicorn app.main:app --host 0.0.0.0 --port 8000 --no-reload

pause

