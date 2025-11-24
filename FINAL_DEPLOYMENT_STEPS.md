# 🚀 FINAL DEPLOYMENT STEPS - Complete Guide

## ⚡ QUICK START (Copy-Paste Commands)

### Step 1: Backend Setup (Terminal 1)

```powershell
# Navigate to project
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\backend"

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# If execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Install dependencies
pip install -r requirements.txt

# Create .env file (use notepad or any editor)
notepad .env
```

**In .env file, paste:**
```env
JWT_SECRET=my-super-secret-key-12345
JWT_ALGO=HS256
GEMINI_API_KEY=your-gemini-api-key-here
DATABASE_URL=sqlite:///./database.db
```

**Save and close.**

```powershell
# Initialize database
python init_database.py

# Start server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**✅ Backend running on http://localhost:8000**

---

### Step 2: Frontend Setup (Terminal 2 - NEW WINDOW)

```powershell
# Navigate to frontend
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator\frontend"

# Install dependencies
npm install

# Create .env file
notepad .env
```

**In .env file, paste:**
```env
VITE_API_URL=http://localhost:8000
```

**Save and close.**

```powershell
# Start frontend
npm run dev
```

**✅ Frontend running on http://localhost:5173**

---

### Step 3: Open Application

1. Open browser
2. Go to: **http://localhost:5173**
3. Register → Login → Create Project → Generate Content

---

## 🌐 DEPLOYMENT TO PRODUCTION

### Option A: Render (Backend) + Vercel (Frontend) - RECOMMENDED

#### 🎯 Backend on Render

**1. Prepare GitHub Repository**
```powershell
# Make sure all code is committed
git add .
git commit -m "Ready for deployment"
git push origin main
```

**2. Create Render Account**
- Go to https://render.com
- Sign up with GitHub
- Connect your repository

**3. Create Web Service**
- Click "New +" → "Web Service"
- Select your repository
- Configure:
  - **Name:** `ai-doc-generator-backend`
  - **Environment:** `Python 3`
  - **Root Directory:** `backend`
  - **Build Command:** `pip install -r requirements.txt`
  - **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

**4. Add Environment Variables**
In Render dashboard → Environment:
```
JWT_SECRET=your-production-secret-key
JWT_ALGO=HS256
GEMINI_API_KEY=your-gemini-api-key
DATABASE_URL=sqlite:///./database.db
```

**5. Deploy**
- Click "Create Web Service"
- Wait 5-10 minutes
- Copy your URL: `https://your-app.onrender.com`

**6. Initialize Database**
- Go to "Shell" tab
- Run: `python init_database.py`

**✅ Backend deployed!**

---

#### 🎯 Frontend on Vercel

**1. Install Vercel CLI**
```powershell
npm install -g vercel
```

**2. Login**
```powershell
vercel login
```

**3. Deploy**
```powershell
cd frontend
vercel
```

**4. Follow Prompts**
- Link to project or create new
- Confirm settings
- Wait for deployment

**5. Add Environment Variable**
- Go to Vercel Dashboard → Project → Settings → Environment Variables
- Add:
  ```
  VITE_API_URL=https://your-backend.onrender.com
  ```
- Replace with your actual Render URL

**6. Redeploy**
- Go to Deployments
- Click "Redeploy" on latest

**✅ Frontend deployed!**

---

### Option B: Railway (All-in-One)

**1. Create Account**
- Go to https://railway.app
- Sign up with GitHub

**2. Create Project**
- New Project → Deploy from GitHub
- Select your repository

**3. Add Backend Service**
- Add Service → Select `backend` folder
- Settings:
  - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
  - Environment Variables:
    ```
    JWT_SECRET=your-secret
    GEMINI_API_KEY=your-key
    DATABASE_URL=sqlite:///./database.db
    ```

**4. Add Frontend Service**
- Add Service → Select `frontend` folder
- Settings:
  - Build Command: `npm install && npm run build`
  - Environment Variables:
    ```
    VITE_API_URL=https://your-backend.railway.app
    ```

**5. Deploy**
- Both services deploy automatically
- Get URLs from Railway dashboard

**✅ Both deployed!**

---

## 🔧 POST-DEPLOYMENT FIXES

### Update CORS in Backend

After deployment, update `backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://your-frontend.vercel.app",  # Add your frontend URL
        "https://your-frontend.netlify.app",  # Or Netlify URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

**Then redeploy backend.**

---

## ✅ VERIFICATION CHECKLIST

After deployment:

- [ ] Backend URL works: `https://your-backend.onrender.com/docs`
- [ ] Frontend URL works: `https://your-frontend.vercel.app`
- [ ] Can register new account
- [ ] Can login
- [ ] Can create project
- [ ] Can generate content
- [ ] Can export documents
- [ ] No CORS errors in browser console
- [ ] No 404 errors

---

## 🐛 COMMON DEPLOYMENT ISSUES

### Issue: "Build failed"
**Solution:**
- Check build logs in Render/Vercel dashboard
- Verify all dependencies in requirements.txt/package.json
- Check for syntax errors

### Issue: "CORS error"
**Solution:**
- Update CORS origins in backend
- Redeploy backend
- Clear browser cache

### Issue: "Database error"
**Solution:**
- Run `python init_database.py` in Render shell
- Check DATABASE_URL is correct

### Issue: "Environment variable not found"
**Solution:**
- Verify variables are set in deployment platform
- Check variable names match exactly
- Redeploy after adding variables

---

## 📞 NEED HELP?

1. Check logs in Render/Vercel dashboard
2. Check browser console for errors
3. Verify all environment variables
4. Test API endpoints at `/docs`

---

## 🎉 SUCCESS!

Your application is now live and ready to use!

**Backend:** https://your-backend.onrender.com  
**Frontend:** https://your-frontend.vercel.app

---

**Last Updated:** All fixes applied and tested ✅

