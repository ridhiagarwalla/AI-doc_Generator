# ✅ HOW TO CHECK EVERYTHING - Complete Guide

## 🎯 Quick Start (Copy These Commands)

### STEP 1: Check Setup (30 seconds)

```powershell
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\backend"
.\venv\Scripts\Activate.ps1
python check_setup.py
```

**✅ Expected:** "ALL CHECKS PASSED!"

**If errors, fix them first!**

---

### STEP 2: Start Backend (1 minute)

```powershell
# Make sure you're in backend directory with venv activated
uvicorn app.main:app --reload
```

**✅ Expected Output:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

**✅ If you see this = Backend is working!**

**Keep this terminal open!**

---

### STEP 3: Test Backend API (30 seconds)

**Option A: Browser Test**
- Open: http://localhost:8000/docs
- ✅ Should see: Swagger UI with all endpoints

**Option B: Script Test**
```powershell
# In NEW terminal
cd backend
.\venv\Scripts\Activate.ps1
pip install requests
python test_api.py
```

**✅ Expected:** All tests passing

---

### STEP 4: Start Frontend (1 minute)

```powershell
# Open NEW PowerShell window
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\frontend"
npm run dev
```

**✅ Expected:**
```
  VITE v7.x.x  ready in xxx ms
  ➜  Local:   http://localhost:5173/
```

**✅ Frontend is running!**

---

### STEP 5: Test Application (2 minutes)

**Open browser:** http://localhost:5173

#### Test 1: Registration
1. Click "Register here"
2. Fill: Name, Email, Password (min 6 chars)
3. Click "Register"
4. **✅ Should:** Success message, redirect to login

#### Test 2: Login
1. Enter email and password
2. Click "Login"
3. **✅ Should:** Redirect to Projects dashboard

#### Test 3: Create Project
1. Click "Create New Project"
2. Fill all steps (Title, Type, Topic, Outline)
3. Click "Create Project"
4. **✅ Should:** Open project editor

#### Test 4: Generate Content
1. Click "Generate Content"
2. Wait 30-60 seconds
3. **✅ Should:** Content appears for each section

#### Test 5: Refine Content
1. Enter refinement: "Make this more formal"
2. Click "Refine"
3. **✅ Should:** Content updates

#### Test 6: Export
1. Click "Export DOCX" or "Export PPTX"
2. **✅ Should:** File downloads

---

## 🔍 VERIFY NO ERRORS

### Check Backend Terminal
- ✅ No red error messages
- ✅ Only INFO messages
- ✅ "Application startup complete" visible

### Check Frontend Terminal
- ✅ No red error messages
- ✅ Shows "ready" message
- ✅ Shows local URL

### Check Browser Console (F12)
- ✅ No red errors
- ✅ No CORS errors
- ✅ No 404 errors
- ✅ No 500 errors

---

## ✅ SUCCESS INDICATORS

**Everything is working if:**

1. ✅ Backend terminal shows "Application startup complete"
2. ✅ Frontend terminal shows "Local: http://localhost:5173"
3. ✅ Can access http://localhost:8000/docs
4. ✅ Can access http://localhost:5173
5. ✅ Can register account
6. ✅ Can login
7. ✅ Can create project
8. ✅ Can generate content
9. ✅ Can export document
10. ✅ No errors anywhere

---

## 🐛 IF SOMETHING DOESN'T WORK

### Backend Won't Start

**Error: "ModuleNotFoundError"**
```powershell
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Error: "Port 8000 in use"**
```powershell
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Error: "Database locked"**
```powershell
# Close all terminals
del database.db
python init_database.py
```

### Frontend Won't Start

**Error: "Cannot find module"**
```powershell
Remove-Item -Recurse -Force node_modules
npm install
```

**Error: "Port 5173 in use"**
- Vite will use next available port automatically

### API Calls Fail

**CORS Error:**
- Check backend is running
- Check `VITE_API_URL` in frontend `.env`

**401 Unauthorized:**
- Try logging in again
- Check token in localStorage

**404 Not Found:**
- Verify backend is running
- Check API endpoint URLs

---

## 📊 QUICK STATUS CHECK

Run these commands to check status:

```powershell
# Check backend
cd backend
.\venv\Scripts\Activate.ps1
python check_setup.py

# Check if backend is running
curl http://localhost:8000

# Check if frontend is running
curl http://localhost:5173
```

---

## 🎉 FINAL VERIFICATION

**Complete this checklist:**

- [ ] `check_setup.py` passes
- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] Can access http://localhost:8000/docs
- [ ] Can access http://localhost:5173
- [ ] Can register account
- [ ] Can login
- [ ] Can create project
- [ ] Can generate content
- [ ] Can export document
- [ ] No errors in any terminal
- [ ] No errors in browser console

**If all checked ✅ = Everything works perfectly!**

---

## 📚 Need More Help?

- **Detailed Steps:** See `COMPLETE_VERIFICATION_STEPS.md`
- **Setup Guide:** See `STEP_BY_STEP_GUIDE.md`
- **Deployment:** See `FINAL_DEPLOYMENT_STEPS.md`

---

**🎉 All corrections complete! Follow the steps above to verify everything works!**

---

**Last Updated:** Complete verification guide ready ✅

