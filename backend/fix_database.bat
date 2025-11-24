@echo off
echo ========================================
echo Fixing Database Schema
echo ========================================
echo.

cd /d "%~dp0"

echo [1/2] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment
    pause
    exit /b 1
)

echo [2/2] Resetting database...
python reset_database_fix.py

pause

