# ⚡ Quick Database Fix

## 🐛 Error: "no such column users_created"

**Quick Fix:** Reset the database to match the current schema.

---

## 🚀 2-Step Fix

### Step 1: Reset Database

```powershell
cd backend
.\venv\Scripts\Activate.ps1
python reset_database_fix.py
```

Type `yes` when prompted.

**OR use the batch file:**
```powershell
cd backend
.\fix_database.bat
```

### Step 2: Restart Backend

```powershell
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## ✅ Done!

After resetting:
- ✅ Database schema matches models
- ✅ All columns exist
- ✅ No more errors
- ✅ Website works smoothly

**Note:** You'll need to register a new account after resetting.

---

**That's it! Your database is now fixed!** 🎉

