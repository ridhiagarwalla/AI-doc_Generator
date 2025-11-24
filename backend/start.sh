#!/bin/bash

# Backend Startup Script

echo "🚀 Starting AI Document Generator Backend..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Check if .env file exists
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found!"
    echo "📝 Please create a .env file with the following variables:"
    echo "   JWT_SECRET=your-secret-key"
    echo "   GEMINI_API_KEY=your-gemini-api-key"
    echo "   DATABASE_URL=sqlite:///./database.db"
    exit 1
fi

# Initialize database
echo "🗄️  Initializing database..."
python init_database.py

# Start server
echo "✅ Starting FastAPI server..."
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

