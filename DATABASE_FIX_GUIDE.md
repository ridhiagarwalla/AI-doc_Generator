# 🔧 Database Error Fix Guide

## 🐛 Error: "no such column users_created"

**Problem:** Database schema is out of sync with models. The database was created with an old schema.

**Solution:** Reset the database to match the current models.

---

## 🚀 Quick Fix (2 Steps)

### Step 1: Reset Database

**Option A: Use the batch file (Easiest)**
```powershell
cd backend
.\fix_database.bat
```
Type `yes` when prompted.

**Option B: Manual reset**
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python reset_database_fix.py
```
Type `yes` when prompted.

### Step 2: Restart Backend

```powershell
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## ✅ Verify Fix

After resetting, you should see:
```
✅ Database reset successfully!
✅ All tables created with correct schema
```

**Tables created:**
- `users` - id, full_name, email, password, created_at
- `projects` - id, user_id, title, doc_type, topic, outline, content, refinement_history, feedback, created_at, updated_at, description
- `content` - id, project_id, section_id, text, created_at, updated_at
- `refinements` - id, project_id, section_id, prompt, updated_text, timestamp

---

## 🔄 Alternative: Reinitialize Database

If reset doesn't work, delete and recreate:

```powershell
cd backend
del database.db
python init_database.py
```

---

## ⚠️ Important Notes

1. **Data Loss:** Resetting the database will DELETE all existing data
2. **Backup:** If you have important data, back it up first
3. **Fresh Start:** After reset, you'll need to register a new account

---

## 🎯 After Fix

1. ✅ Database schema matches models
2. ✅ All columns exist
3. ✅ No more "no such column" errors
4. ✅ Registration works
5. ✅ Login works
6. ✅ Projects work

---

## 📋 Database Schema

### Users Table
- `id` (Integer, Primary Key)
- `full_name` (String)
- `email` (String, Unique)
- `password` (String)
- `created_at` (DateTime)

### Projects Table
- `id` (Integer, Primary Key)
- `user_id` (Integer, Foreign Key)
- `title` (String)
- `doc_type` (String, Nullable)
- `topic` (Text, Nullable)
- `outline` (JSON)
- `content` (JSON)
- `refinement_history` (JSON)
- `feedback` (JSON)
- `created_at` (DateTime)
- `updated_at` (DateTime)
- `description` (Text, Nullable)

### Content Table
- `id` (Integer, Primary Key)
- `project_id` (Integer, Foreign Key)
- `section_id` (String)
- `text` (Text)
- `created_at` (DateTime)
- `updated_at` (DateTime)

### Refinements Table
- `id` (Integer, Primary Key)
- `project_id` (Integer, Foreign Key)
- `section_id` (String)
- `prompt` (Text)
- `updated_text` (Text)
- `timestamp` (DateTime)

---

**After fixing, your website should work smoothly!** 🎉

