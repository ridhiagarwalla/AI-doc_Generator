# PowerShell Script to Test Setup
# Run this to verify everything is configured correctly

Write-Host "🔍 Testing AI Document Generator Setup..." -ForegroundColor Cyan
Write-Host ""

# Check Python
Write-Host "1. Checking Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "   ✅ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Python not found! Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Check Node.js
Write-Host "2. Checking Node.js..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    Write-Host "   ✅ Node.js found: $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "   ❌ Node.js not found! Please install Node.js 16+" -ForegroundColor Red
    exit 1
}

# Check Backend .env
Write-Host "3. Checking backend .env file..." -ForegroundColor Yellow
if (Test-Path "backend\.env") {
    Write-Host "   ✅ Backend .env file exists" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Backend .env file not found!" -ForegroundColor Yellow
    Write-Host "   📝 Create backend\.env with: JWT_SECRET, GEMINI_API_KEY, DATABASE_URL" -ForegroundColor Yellow
}

# Check Frontend .env
Write-Host "4. Checking frontend .env file..." -ForegroundColor Yellow
if (Test-Path "frontend\.env") {
    Write-Host "   ✅ Frontend .env file exists" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Frontend .env file not found!" -ForegroundColor Yellow
    Write-Host "   📝 Create frontend\.env with: VITE_API_URL=http://localhost:8000" -ForegroundColor Yellow
}

# Check Backend venv
Write-Host "5. Checking backend virtual environment..." -ForegroundColor Yellow
if (Test-Path "backend\venv") {
    Write-Host "   ✅ Virtual environment exists" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Virtual environment not found!" -ForegroundColor Yellow
    Write-Host "   📝 Run: cd backend && python -m venv venv" -ForegroundColor Yellow
}

# Check Backend requirements
Write-Host "6. Checking backend requirements.txt..." -ForegroundColor Yellow
if (Test-Path "backend\requirements.txt") {
    Write-Host "   ✅ requirements.txt exists" -ForegroundColor Green
} else {
    Write-Host "   ❌ requirements.txt not found!" -ForegroundColor Red
}

# Check Frontend package.json
Write-Host "7. Checking frontend package.json..." -ForegroundColor Yellow
if (Test-Path "frontend\package.json") {
    Write-Host "   ✅ package.json exists" -ForegroundColor Green
} else {
    Write-Host "   ❌ package.json not found!" -ForegroundColor Red
}

# Check Database
Write-Host "8. Checking database..." -ForegroundColor Yellow
if (Test-Path "backend\database.db") {
    Write-Host "   ✅ Database file exists" -ForegroundColor Green
} else {
    Write-Host "   ⚠️  Database not initialized!" -ForegroundColor Yellow
    Write-Host "   📝 Run: cd backend && python init_database.py" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "✅ Setup check complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Start backend: cd backend && .\venv\Scripts\Activate.ps1 && uvicorn app.main:app --reload" -ForegroundColor White
Write-Host "2. Start frontend: cd frontend && npm run dev" -ForegroundColor White
Write-Host "3. Open browser: http://localhost:5173" -ForegroundColor White

