# 🏠 LOCAL HOSTING GUIDE - Complete Setup

## 🎯 Quick Start (No Reload Issues)

### STEP 1: Setup Backend (One Time)

```powershell
# Navigate to backend
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\backend"

# Create virtual environment (if not exists)
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install all dependencies
pip install -r requirements.txt
```

### STEP 2: Create Environment File

```powershell
# Create .env file
notepad .env
```

**Copy and paste this (replace with your actual values):**
```env
JWT_SECRET=my-super-secret-jwt-key-12345
JWT_ALGO=HS256
GEMINI_API_KEY=your-actual-gemini-api-key-here
DATABASE_URL=sqlite:///./database.db
```

**Save and close.**

### STEP 3: Initialize Database

```powershell
# Make sure venv is activated
python init_database.py
```

**Expected:** ✅ Database initialized successfully!

### STEP 4: Start Backend (NO RELOAD)

```powershell
# Use the start script (prevents reload loops)
python start_server.py
```

**OR use uvicorn directly (without reload):**
```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000 --no-reload
```

**Expected Output:**
```
✅ Database tables ready
🚀 Starting server...
📡 Backend will be available at: http://localhost:8000
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**✅ Backend is running! Keep this terminal open.**

---

### STEP 5: Setup Frontend (One Time)

```powershell
# Open NEW terminal window
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\frontend"

# Install dependencies
npm install
```

### STEP 6: Create Frontend Environment File

```powershell
notepad .env
```

**Copy and paste:**
```env
VITE_API_URL=http://localhost:8000
```

**Save and close.**

### STEP 7: Start Frontend

```powershell
npm run dev
```

**Expected:**
```
  VITE v7.x.x  ready in xxx ms
  ➜  Local:   http://localhost:5173/
```

**✅ Frontend is running!**

---

### STEP 8: Access Application

**Open browser:** http://localhost:5173

**✅ Application is ready!**

---

## 🔧 FIXING RELOAD LOOPS

### Problem: Server Reloads Multiple Times

**Solution 1: Use start_server.py (Recommended)**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python start_server.py
```

**Solution 2: Disable Reload**
```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000 --no-reload
```

**Solution 3: Use Specific Reload Directories**
```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir app
```

---

## ✅ VERIFICATION STEPS

### 1. Check Backend is Running

**Open:** http://localhost:8000

**Should see:**
```json
{
  "message": "AI Document Generator API",
  "docs": "/docs",
  "version": "1.0.0"
}
```

### 2. Check API Documentation

**Open:** http://localhost:8000/docs

**Should see:** Swagger UI with all endpoints

### 3. Check Frontend

**Open:** http://localhost:5173

**Should see:** Login page

### 4. Test Registration

1. Click "Register here"
2. Fill form
3. Click "Register"
4. **Should:** Success message

### 5. Test Login

1. Enter credentials
2. Click "Login"
3. **Should:** Redirect to dashboard

---

## 🐛 TROUBLESHOOTING

### Issue: Server Keeps Reloading

**Fix:**
```powershell
# Use start_server.py instead
python start_server.py

# OR disable reload
uvicorn app.main:app --no-reload
```

### Issue: Import Errors

**Fix:**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Issue: Database Errors

**Fix:**
```powershell
del database.db
python init_database.py
```

### Issue: Port Already in Use

**Fix:**
```powershell
# Find process
netstat -ano | findstr :8000

# Kill process (replace PID)
taskkill /PID <PID> /F
```

---

## 📝 COMPLETE COMMAND REFERENCE

### Backend Commands
```powershell
# Setup (one time)
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Create .env file
notepad .env

# Initialize database
python init_database.py

# Start server (NO RELOAD - prevents loops)
python start_server.py
```

### Frontend Commands
```powershell
# Setup (one time)
cd frontend
npm install

# Create .env file
notepad .env

# Start server
npm run dev
```

---

## ✅ SUCCESS CHECKLIST

- [ ] Backend starts without reload loops
- [ ] Can access http://localhost:8000
- [ ] Can access http://localhost:8000/docs
- [ ] Frontend starts without errors
- [ ] Can access http://localhost:5173
- [ ] Can register account
- [ ] Can login
- [ ] Can create project
- [ ] Can generate content
- [ ] Can export document

---

## 🎉 READY!

**Your application is now running locally without reload issues!**

**Backend:** http://localhost:8000  
**Frontend:** http://localhost:5173

---

**Last Updated:** Local hosting guide complete ✅

