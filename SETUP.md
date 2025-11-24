# Quick Setup Guide

## Backend Environment Variables

Create a file named `.env` in the `backend/` directory with the following content:

```env
JWT_SECRET=your-secret-key-change-this-in-production
JWT_ALGO=HS256
GEMINI_API_KEY=your-gemini-api-key-here
DATABASE_URL=sqlite:///./database.db
```

**Important**: 
- Replace `your-secret-key-change-this-in-production` with a strong random string
- Get your Gemini API key from: https://makersuite.google.com/app/apikey

## Frontend Environment Variables

Create a file named `.env` in the `frontend/` directory with the following content:

```env
VITE_API_URL=http://localhost:8000
```

For production, update this to your backend URL (e.g., `https://your-backend.onrender.com`)

## Quick Start Commands

### Backend
```bash
cd backend
python -m venv venv
# Activate venv (Windows: venv\Scripts\activate, Linux/Mac: source venv/bin/activate)
pip install -r requirements.txt
# Create .env file (see above)
python -m app.init_db  # Initialize database
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
npm install
# Create .env file (see above)
npm run dev
```

## Testing the Application

1. Start the backend server (port 8000)
2. Start the frontend server (port 5173)
3. Open http://localhost:5173 in your browser
4. Register a new account
5. Create a project and start generating documents!

