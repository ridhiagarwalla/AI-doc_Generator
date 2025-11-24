# 🚀 Quick Start Guide

## Prerequisites
- Python 3.8+ installed
- Node.js 16+ installed
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

## Step 1: Backend Setup

### Windows:
```bash
cd backend
start.bat
```

### Linux/Mac:
```bash
cd backend
chmod +x start.sh
./start.sh
```

### Manual Setup:
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Linux/Mac)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
# Copy the content below and save as .env
```

**Create `backend/.env` file:**
```env
JWT_SECRET=your-random-secret-key-here
JWT_ALGO=HS256
GEMINI_API_KEY=your-gemini-api-key-here
DATABASE_URL=sqlite:///./database.db
```

```bash
# Initialize database
python init_database.py

# Start server
uvicorn app.main:app --reload
```

Backend will run on: `http://localhost:8000`

## Step 2: Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Create .env file
# Copy the content below and save as .env
```

**Create `frontend/.env` file:**
```env
VITE_API_URL=http://localhost:8000
```

```bash
# Start development server
npm run dev
```

Frontend will run on: `http://localhost:5173`

## Step 3: Test the Application

1. Open `http://localhost:5173` in your browser
2. Click "Register" to create an account
3. Login with your credentials
4. Click "Create New Project"
5. Follow the wizard to create a project
6. Generate content and export documents!

## Common Issues

### Backend won't start
- ✅ Check if port 8000 is available
- ✅ Verify .env file exists and has correct values
- ✅ Ensure virtual environment is activated
- ✅ Run `python init_database.py` to initialize database

### Frontend won't start
- ✅ Check if port 5173 is available
- ✅ Verify .env file exists with VITE_API_URL
- ✅ Delete `node_modules` and run `npm install` again

### API Connection Errors
- ✅ Verify backend is running on port 8000
- ✅ Check CORS settings in `backend/app/main.py`
- ✅ Verify `VITE_API_URL` in frontend .env file

### Gemini API Errors
- ✅ Verify GEMINI_API_KEY is correct
- ✅ Check API quota limits
- ✅ Ensure API key has proper permissions

## Need Help?

Check the full documentation in `README.md` for detailed setup instructions and troubleshooting.

