# ✅ COMPLETE VERIFICATION STEPS - Test Everything

## 🎯 Step-by-Step Verification Guide

Follow these steps in order to verify everything works correctly.

---

## 📋 PRE-FLIGHT CHECKS

### Step 1: Verify Setup

```powershell
# Navigate to backend
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\backend"

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run setup checker
python check_setup.py
```

**Expected Output:**
```
✅ Python version OK
✅ .env file found
✅ Database exists
✅ All imports successful
✅ All dependencies installed
✅ ALL CHECKS PASSED!
```

**If errors appear, fix them before proceeding.**

---

### Step 2: Verify Environment Variables

```powershell
# Check .env file exists
dir .env

# View .env content (make sure it has values, not placeholders)
notepad .env
```

**Required in `.env`:**
```env
JWT_SECRET=your-actual-secret-key-here
JWT_ALGO=HS256
GEMINI_API_KEY=your-actual-gemini-api-key
DATABASE_URL=sqlite:///./database.db
```

**Important:** Replace placeholders with actual values!

---

### Step 3: Initialize Database (if needed)

```powershell
# Check if database exists
dir database.db

# If not exists, initialize
python init_database.py
```

**Expected Output:**
```
✅ Database initialized successfully!
✅ All tables created: users, projects, content, refinements
```

---

## 🚀 START BACKEND SERVER

### Step 4: Start Backend

```powershell
# Make sure you're in backend directory with venv activated
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\backend"
.\venv\Scripts\Activate.ps1

# Start server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected Output (NO ERRORS):**
```
INFO:     Will watch for changes in these directories: ['C:\\Users\\Ridhi Agarwalla\\ai-doc-generator\\backend']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**✅ If you see this, backend is running correctly!**

**Keep this terminal open!**

---

## 🧪 TEST BACKEND API

### Step 5: Test API Endpoints

**Open a NEW browser tab and test:**

1. **Root Endpoint:**
   - Go to: http://localhost:8000
   - Should see: `{"message":"AI Document Generator API","docs":"/docs","version":"1.0.0"}`

2. **API Documentation:**
   - Go to: http://localhost:8000/docs
   - Should see: Swagger UI with all endpoints listed
   - ✅ All endpoints should be visible

3. **Test Registration (in Swagger UI):**
   - Click on `POST /auth/register`
   - Click "Try it out"
   - Enter:
     ```json
     {
       "full_name": "Test User",
       "email": "test@example.com",
       "password": "test123456"
     }
     ```
   - Click "Execute"
   - **Expected:** `200 OK` with success message
   - ✅ Registration works!

4. **Test Login (in Swagger UI):**
   - Click on `POST /auth/login`
   - Click "Try it out"
   - Enter:
     ```json
     {
       "email": "test@example.com",
       "password": "test123456"
     }
     ```
   - Click "Execute"
   - **Expected:** `200 OK` with `access_token`
   - ✅ Login works!

---

## 🎨 START FRONTEND

### Step 6: Start Frontend (New Terminal)

```powershell
# Open NEW PowerShell window
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\frontend"

# Install dependencies (if not done)
npm install

# Check .env file
notepad .env
```

**Make sure `.env` has:**
```env
VITE_API_URL=http://localhost:8000
```

**Then start frontend:**
```powershell
npm run dev
```

**Expected Output:**
```
  VITE v7.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**✅ Frontend is running!**

---

## 🌐 TEST FRONTEND APPLICATION

### Step 7: Test Complete Flow

**Open browser:** http://localhost:5173

#### 7.1 Test Registration
1. Click "Register here" or go to Register page
2. Fill in:
   - Full Name: `Test User`
   - Email: `test@example.com`
   - Password: `test123456`
3. Click "Register"
4. **Expected:** Success message, redirected to login
5. ✅ Registration works!

#### 7.2 Test Login
1. Enter email: `test@example.com`
2. Enter password: `test123456`
3. Click "Login"
4. **Expected:** Redirected to Projects dashboard
5. ✅ Login works!

#### 7.3 Test Project Creation
1. Click "Create New Project"
2. **Step 1:**
   - Title: `My Test Project`
   - Description: `Test description`
   - Select: Word Document (or PowerPoint)
3. Click "Next"
4. **Step 2:**
   - Topic: `Market analysis of electric vehicles in 2025`
5. Click "Next"
6. **Step 3:**
   - **For Word:** Add sections manually or click "✨ AI Suggest Outline"
   - **For PowerPoint:** Enter number of slides and titles
7. Click "Create Project"
8. **Expected:** Redirected to project editor
9. ✅ Project creation works!

#### 7.4 Test Content Generation
1. In project editor, click "Generate Content"
2. Wait 30-60 seconds
3. **Expected:** Content appears for each section/slide
4. ✅ Content generation works!

#### 7.5 Test Content Refinement
1. For any section, enter refinement prompt: `Make this more formal`
2. Click "Refine"
3. Wait a few seconds
4. **Expected:** Content updates
5. ✅ Refinement works!

#### 7.6 Test Feedback
1. Click "👍 Like" or "👎 Dislike" on a section
2. Add a comment in the comment box
3. Click "Add"
4. **Expected:** Feedback saved
5. ✅ Feedback works!

#### 7.7 Test Export
1. Click "Export DOCX" or "Export PPTX"
2. **Expected:** File downloads automatically
3. Open the downloaded file
4. **Expected:** Document contains your content
5. ✅ Export works!

---

## 🔍 VERIFY IN BROWSER CONSOLE

### Step 8: Check for Errors

1. **Open Browser Developer Tools:**
   - Press `F12` or `Ctrl+Shift+I`
   - Go to "Console" tab

2. **Check for Errors:**
   - Should see no red errors
   - ✅ No CORS errors
   - ✅ No 404 errors
   - ✅ No 500 errors

3. **Check Network Tab:**
   - Go to "Network" tab
   - Perform actions (login, create project, etc.)
   - All requests should be `200 OK` or `201 Created`
   - ✅ No failed requests

---

## 📊 VERIFY DATABASE

### Step 9: Check Database

```powershell
# In backend directory
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\backend"
.\venv\Scripts\Activate.ps1

# Check database file exists
dir database.db

# Check database content (optional - requires sqlite3)
python -c "import sqlite3; conn = sqlite3.connect('database.db'); print('Tables:', [row[0] for row in conn.execute(\"SELECT name FROM sqlite_master WHERE type='table'\").fetchall()]); conn.close()"
```

**Expected:** Should see tables: `users`, `projects`, `content`, `refinements`

---

## ✅ FINAL CHECKLIST

After completing all steps above, verify:

- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] Can access http://localhost:8000/docs
- [ ] Can access http://localhost:5173
- [ ] Registration works
- [ ] Login works
- [ ] Can create project
- [ ] Can generate content (if GEMINI_API_KEY is set)
- [ ] Can refine content
- [ ] Can submit feedback
- [ ] Can export document
- [ ] No errors in browser console
- [ ] No errors in backend terminal
- [ ] Database file exists
- [ ] All API calls return success

---

## 🐛 TROUBLESHOOTING

### If Backend Won't Start

**Error: "ModuleNotFoundError"**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Error: "Port 8000 already in use"**
```powershell
# Find and kill process
netstat -ano | findstr :8000
taskkill /PID <process_id> /F
```

**Error: "Database locked"**
```powershell
# Close all terminals
# Delete and recreate
del database.db
python init_database.py
```

### If Frontend Won't Start

**Error: "Cannot find module"**
```powershell
Remove-Item -Recurse -Force node_modules
npm install
```

**Error: "Port 5173 already in use"**
- Vite will automatically use next available port
- Check terminal for actual port number

### If API Calls Fail

**CORS Error:**
- Verify backend CORS settings in `backend/app/main.py`
- Make sure frontend URL is in `allow_origins`

**401 Unauthorized:**
- Check if token is being saved: `localStorage.getItem("token")` in browser console
- Try logging in again

**404 Not Found:**
- Verify backend is running on port 8000
- Check `VITE_API_URL` in frontend `.env`

---

## 🎉 SUCCESS INDICATORS

You'll know everything works when:

1. ✅ Backend shows "Application startup complete"
2. ✅ Frontend shows "Local: http://localhost:5173"
3. ✅ Can register and login
4. ✅ Can create projects
5. ✅ Can generate content
6. ✅ Can export documents
7. ✅ No errors in console
8. ✅ All features work smoothly

---

## 📝 QUICK TEST COMMANDS

### Test Backend API Directly

```powershell
# Test registration
curl -X POST "http://localhost:8000/auth/register" -H "Content-Type: application/json" -d "{\"full_name\":\"Test\",\"email\":\"test@test.com\",\"password\":\"test123\"}"

# Test login
curl -X POST "http://localhost:8000/auth/login" -H "Content-Type: application/json" -d "{\"email\":\"test@test.com\",\"password\":\"test123\"}"
```

---

## 🎯 SUMMARY

**Complete these steps in order:**
1. ✅ Run `python check_setup.py`
2. ✅ Start backend server
3. ✅ Test API at http://localhost:8000/docs
4. ✅ Start frontend server
5. ✅ Test complete flow in browser
6. ✅ Verify no errors in console
7. ✅ Test all features

**If all steps pass, your application is working perfectly! 🎉**

---

**Last Updated:** Complete verification guide ready ✅

