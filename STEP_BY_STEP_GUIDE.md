# 📋 Complete Step-by-Step Guide to Run the Application

## Prerequisites Check

First, verify you have everything installed:

```powershell
# Check Python version (should be 3.8+)
python --version

# Check Node.js version (should be 16+)
node --version

# Check npm version
npm --version
```

If any are missing, install them first.

---

## 🎯 STEP 1: Backend Setup (Terminal Commands)

### Open PowerShell/Terminal and follow these steps:

```powershell
# Navigate to project directory
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator"

# Go to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment (Windows PowerShell)
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate again:
.\venv\Scripts\Activate.ps1

# Install all dependencies
pip install -r requirements.txt
```

### Create Backend .env File

```powershell
# Create .env file in backend directory
# You can use notepad or any text editor
notepad .env
```

**Copy and paste this into the .env file:**
```env
JWT_SECRET=your-super-secret-key-change-this-12345
JWT_ALGO=HS256
GEMINI_API_KEY=your-gemini-api-key-here
DATABASE_URL=sqlite:///./database.db
```

**Important:** Replace `your-gemini-api-key-here` with your actual Gemini API key from https://makersuite.google.com/app/apikey

**Save and close the file.**

### Initialize Database

```powershell
# Make sure you're in backend directory and venv is activated
python init_database.py
```

You should see: `✅ Database initialized successfully!`

### Start Backend Server

```powershell
# Start the FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**You should see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**✅ Backend is now running! Keep this terminal window open.**

**Test it:** Open browser and go to: http://localhost:8000/docs

---

## 🎯 STEP 2: Frontend Setup (New Terminal Window)

### Open a NEW PowerShell/Terminal window:

```powershell
# Navigate to project directory
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator"

# Go to frontend folder
cd frontend

# Install all dependencies
npm install
```

This may take a few minutes. Wait for it to complete.

### Create Frontend .env File

```powershell
# Create .env file in frontend directory
notepad .env
```

**Copy and paste this:**
```env
VITE_API_URL=http://localhost:8000
```

**Save and close the file.**

### Start Frontend Server

```powershell
# Start the development server
npm run dev
```

**You should see:**
```
  VITE v7.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**✅ Frontend is now running!**

---

## 🎯 STEP 3: Access the Application

1. **Open your web browser**
2. **Go to:** http://localhost:5173
3. **You should see the login page**

---

## 🎯 STEP 4: Test the Application

### 1. Register a New Account
   - Click "Register here" or go to Register page
   - Fill in:
     - Full Name: Your Name
     - Email: your-email@example.com
     - Password: (at least 6 characters)
   - Click "Register"
   - You'll be redirected to login

### 2. Login
   - Enter your email and password
   - Click "Login"
   - You'll be redirected to the Projects dashboard

### 3. Create a Project
   - Click "Create New Project"
   - **Step 1:** Enter title, description, select document type (Word or PowerPoint)
   - **Step 2:** Enter topic (e.g., "Market analysis of EV industry")
   - **Step 3:** 
     - For Word: Add sections manually or click "AI Suggest Outline"
     - For PowerPoint: Enter number of slides and titles
   - Click "Create Project"

### 4. Generate Content
   - Click "Open" on your project
   - Click "Generate Content" button
   - Wait for content to generate (may take 30-60 seconds)

### 5. Refine Content
   - For each section, you can:
     - Enter refinement prompt (e.g., "Make it more formal")
     - Click "Refine"
     - Use Like/Dislike buttons
     - Add comments

### 6. Export Document
   - Click "Export DOCX" or "Export PPTX" button
   - Document will download automatically

---

## 🐛 Troubleshooting Common Errors

### Error: "ModuleNotFoundError: No module named 'app'"

**Solution:**
```powershell
# Make sure you're in the backend directory
cd backend

# Make sure venv is activated (you should see (venv) in prompt)
.\venv\Scripts\Activate.ps1

# Try running again
uvicorn app.main:app --reload
```

### Error: "Port 8000 is already in use"

**Solution:**
```powershell
# Find what's using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F

# Or use a different port
uvicorn app.main:app --reload --port 8001
```

### Error: "Cannot find module" in frontend

**Solution:**
```powershell
cd frontend
# Delete node_modules and reinstall
Remove-Item -Recurse -Force node_modules
npm install
```

### Error: "GEMINI_API_KEY not set"

**Solution:**
- Make sure `.env` file exists in `backend/` directory
- Check that the file has `GEMINI_API_KEY=your-actual-key`
- Restart the backend server after creating/updating .env

### Error: "CORS error" in browser

**Solution:**
- Make sure backend is running on port 8000
- Make sure frontend .env has `VITE_API_URL=http://localhost:8000`
- Check browser console for exact error

### Error: "Execution Policy" when activating venv

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Then try activating again
.\venv\Scripts\Activate.ps1
```

---

## 📝 Quick Command Reference

### Backend Commands
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python init_database.py
uvicorn app.main:app --reload
```

### Frontend Commands
```powershell
cd frontend
npm install
npm run dev
```

### Stop Servers
- Press `CTRL + C` in the terminal where server is running

---

## ✅ Verification Checklist

Before testing, ensure:

- [ ] Backend server is running (see "Application startup complete")
- [ ] Frontend server is running (see "Local: http://localhost:5173")
- [ ] Backend .env file exists with GEMINI_API_KEY
- [ ] Frontend .env file exists with VITE_API_URL
- [ ] Database initialized (database.db file exists in backend/)
- [ ] No errors in terminal windows

---

## 🚀 Next Steps

Once everything is running:
1. Test all features
2. Create projects
3. Generate and export documents
4. Check the API docs at http://localhost:8000/docs

---

**Need more help?** Check `README.md` for detailed documentation.

