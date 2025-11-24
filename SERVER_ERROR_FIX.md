# 🔧 Server Error Fix Guide

## ✅ Fixes Applied

1. **Global Exception Handler** - Catches all unhandled errors
2. **Better Error Logging** - Shows detailed error information
3. **Health Check Endpoint** - `/health` to test server status
4. **Improved Error Handling** - Better error messages for debugging

---

## 🚀 How to Fix Server Errors

### Step 1: Restart Backend

```powershell
# Stop current backend (Ctrl+C)
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Step 2: Check Health

Open: http://localhost:8000/health

**Should return:**
```json
{
  "status": "healthy",
  "database": "connected"
}
```

### Step 3: Check Backend Terminal

**Look for:**
- `✅ Database tables ready` - Database is OK
- `❌ Unhandled exception:` - Shows the actual error
- Error traceback - Shows where the error occurred

---

## 🐛 Common Server Errors & Fixes

### Error: "Internal server error"

**Solution:**
1. Check backend terminal for error details
2. Look for the error message after `❌ Unhandled exception:`
3. Fix the specific issue shown

### Error: "Database error"

**Solution:**
```powershell
cd backend
del database.db
python init_database.py
```

### Error: "Module not found"

**Solution:**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Error: "Port already in use"

**Solution:**
1. Find process using port 8000
2. Kill it or use different port:
```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8001
```

---

## 🧪 Test Endpoints

### 1. Health Check
```powershell
curl http://localhost:8000/health
```

### 2. Root Endpoint
```powershell
curl http://localhost:8000/
```

### 3. API Docs
Open: http://localhost:8000/docs

---

## 📝 What Changed

### `backend/app/main.py`
- ✅ Added global exception handler
- ✅ Added validation error handler
- ✅ Added health check endpoint
- ✅ Better error logging

### `backend/app/auth/routes.py`
- ✅ Improved error handling in login
- ✅ Better error messages

---

## ✅ Verification

After restarting:

1. **Health check works:** http://localhost:8000/health
2. **API docs work:** http://localhost:8000/docs
3. **No errors in terminal:** Backend starts cleanly
4. **Registration works:** Can create account
5. **Login works:** Can login

---

**The server should now handle errors gracefully and show clear error messages!**

