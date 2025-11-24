# 🚀 OpenRouter API Setup - Quick Guide

## ✅ Code Updated!

All code has been updated to use OpenRouter API instead of Gemini.

---

## 🔑 Step 1: Create .env File

Create a file named `.env` in the `backend/` directory with this content:

```env
# OpenRouter API Key
OPENROUTER_API_KEY=sk-or-v1 a8410c138be36f6be22d829b8491f8be771666418341afdf7a07c2d57182b134

# JWT Secret Key
JWT_SECRET=9a93535b8efd8813b0b819116cc827ea8c00ebed43caef498dfcece7895533b7
```

**File location:** `backend/.env`

---

## 🚀 Step 2: Restart Backend

```powershell
# Stop current backend (Ctrl+C)
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

**You should see:**
```
✅ OpenRouter API configured
✅ Database tables ready
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

## ✅ Step 3: Test It!

1. Go to: http://localhost:5173
2. Login or Register
3. Create a new project
4. Try generating content
5. **Should work perfectly!** ✅

---

## 🎉 Done!

Your backend is now using OpenRouter API for all AI content generation!

**No more errors - content generation will work smoothly!** 🚀

