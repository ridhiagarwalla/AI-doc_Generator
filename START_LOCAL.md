# 🚀 START APPLICATION LOCALLY - No Reload Issues

## ⚡ QUICK START (Copy These Commands)

### Terminal 1 - Backend

```powershell
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\backend"
.\venv\Scripts\Activate.ps1
python start_server.py
```

**✅ This prevents reload loops!**

---

### Terminal 2 - Frontend

```powershell
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\frontend"
npm run dev
```

---

### Open Browser

**http://localhost:5173**

---

## 📋 COMPLETE SETUP (First Time Only)

### Backend Setup

```powershell
# 1. Navigate to backend
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\backend"

# 2. Create virtual environment
python -m venv venv

# 3. Activate
.\venv\Scripts\Activate.ps1

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create .env file
notepad .env
```

**In .env file, paste:**
```env
JWT_SECRET=my-secret-key-12345
JWT_ALGO=HS256
GEMINI_API_KEY=your-gemini-api-key
DATABASE_URL=sqlite:///./database.db
```

**Save and close.**

```powershell
# 6. Initialize database
python init_database.py

# 7. Start server (NO RELOAD - prevents loops)
python start_server.py
```

---

### Frontend Setup

```powershell
# 1. Navigate to frontend
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\frontend"

# 2. Install dependencies
npm install

# 3. Create .env file
notepad .env
```

**In .env file, paste:**
```env
VITE_API_URL=http://localhost:8000
```

**Save and close.**

```powershell
# 4. Start frontend
npm run dev
```

---

## ✅ VERIFICATION

### Check Backend
- Open: http://localhost:8000
- Should see: API message
- Open: http://localhost:8000/docs
- Should see: Swagger UI

### Check Frontend
- Open: http://localhost:5173
- Should see: Login page

### Test Application
1. Register account
2. Login
3. Create project
4. Generate content
5. Export document

**✅ Everything works!**

---

## 🔧 IF RELOAD LOOPS STILL HAPPEN

**Use this command instead:**
```powershell
uvicorn app.main:app --host 0.0.0.0 --port 8000 --no-reload
```

**This completely disables reload and prevents loops.**

---

## 📝 FILES TO CHECK

### Backend
- ✅ `backend/.env` exists with real values
- ✅ `backend/database.db` exists
- ✅ `backend/venv/` exists

### Frontend
- ✅ `frontend/.env` exists with `VITE_API_URL`
- ✅ `frontend/node_modules/` exists

---

**🎉 Application ready to run locally!**

