# 🚀 START HERE - Complete Setup Guide

## ⚠️ CRITICAL FIX APPLIED

**The main issue was fixed:** CORS middleware was incorrectly placed, preventing frontend-backend communication. This is now fixed!

---

## 🎯 Quick Start (3 Steps)

### Step 1: Initialize Database

```powershell
cd backend
.\venv\Scripts\Activate.ps1
python init_database.py
```

**Expected:** `✅ Database initialized successfully!`

### Step 2: Start Backend

**Option A: Use the batch file (Easiest)**
```powershell
cd backend
.\start_backend.bat
```

**Option B: Manual start**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**Expected:** 
```
✅ Database tables ready
INFO:     Uvicorn running on http://0.0.0.0:8000
```

### Step 3: Start Frontend (New Terminal)

```powershell
cd frontend
npm install
npm run dev
```

**Expected:** `Local: http://localhost:5173/`

---

## ✅ Verify Everything Works

### 1. Check Backend
- Open: http://localhost:8000/docs
- Should see Swagger UI

### 2. Check Frontend
- Open: http://localhost:5173
- Should see login page

### 3. Test Registration
- Go to: http://localhost:5173/register
- Fill form and register
- Should see success message

### 4. Test Login
- Go to: http://localhost:5173/login
- Login with registered credentials
- Should redirect to projects page

---

## 🔧 If Something Doesn't Work

### Backend Health Check

```powershell
cd backend
.\venv\Scripts\Activate.ps1
python check_backend.py
```

This will tell you exactly what's wrong!

### Common Issues

**Issue: "Cannot connect to server"**
- ✅ Make sure backend is running on port 8000
- ✅ Check CORS is fixed (already done)

**Issue: "Database error"**
```powershell
cd backend
del database.db
python init_database.py
```

**Issue: "Registration failed"**
- Check backend terminal for error details
- Run `python check_backend.py`
- Check browser console (F12)

---

## 📋 What Was Fixed

1. ✅ **CORS Middleware** - Fixed placement (was inside startup function)
2. ✅ **Database Path** - Fixed Windows compatibility
3. ✅ **Error Handling** - Better error messages
4. ✅ **Registration Flow** - Improved validation and error handling

---

## 🎉 You're All Set!

Follow the 3 steps above and everything should work perfectly!

**Need help?** Check `COMPLETE_FIX_GUIDE.md` for detailed troubleshooting.
