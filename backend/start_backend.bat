@echo off
echo ========================================
echo Starting AI Document Generator Backend
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    echo Make sure venv exists. Run: python -m venv venv
    pause
    exit /b 1
)

echo [2/3] Checking database...
python init_database.py
if errorlevel 1 (
    echo ERROR: Database initialization failed
    pause
    exit /b 1
)

echo [3/3] Starting server...
echo.
echo Backend will be available at: http://localhost:8000
echo API docs will be available at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo.

uvicorn app.main:app --host 0.0.0.0 --port 8000

pause

