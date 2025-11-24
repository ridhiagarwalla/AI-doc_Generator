# 🚀 Complete Setup & Deployment Guide

## 📋 Table of Contents
1. [Local Development Setup](#local-development-setup)
2. [Running the Application](#running-the-application)
3. [Deployment to Production](#deployment-to-production)
4. [Troubleshooting](#troubleshooting)

---

## 🛠️ LOCAL DEVELOPMENT SETUP

### Prerequisites
- Python 3.8 or higher
- Node.js 16 or higher
- npm or yarn
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))

### Step 1: Backend Setup

Open **PowerShell** or **Command Prompt** and run:

```powershell
# Navigate to project root
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator"

# Go to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# For PowerShell:
.\venv\Scripts\Activate.ps1

# If you get execution policy error, run this first:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# For Command Prompt (cmd):
venv\Scripts\activate.bat

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Create Backend Environment File

```powershell
# Create .env file
notepad .env
```

**Copy this content into the file:**
```env
JWT_SECRET=your-super-secret-jwt-key-change-this-in-production-12345
JWT_ALGO=HS256
GEMINI_API_KEY=your-actual-gemini-api-key-here
DATABASE_URL=sqlite:///./database.db
```

**Important:** 
- Replace `your-actual-gemini-api-key-here` with your real Gemini API key
- Save the file (Ctrl+S) and close Notepad

### Step 3: Initialize Database

```powershell
# Make sure you're in backend directory and venv is activated
python init_database.py
```

**Expected output:**
```
✅ Database initialized successfully!
✅ All tables created: users, projects, content, refinements
```

### Step 4: Start Backend Server

```powershell
# Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**Expected output:**
```
INFO:     Will watch for changes
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**✅ Backend is running!** Keep this terminal open.

**Test:** Open browser → http://localhost:8000/docs (should show API documentation)

---

### Step 5: Frontend Setup (New Terminal)

Open a **NEW** PowerShell/Command Prompt window:

```powershell
# Navigate to project root
cd "C:\Users\Ridhi Agarwalla\ai-doc-generator"

# Go to frontend directory
cd frontend

# Install dependencies (this may take 2-3 minutes)
npm install
```

### Step 6: Create Frontend Environment File

```powershell
# Create .env file
notepad .env
```

**Copy this content:**
```env
VITE_API_URL=http://localhost:8000
```

**Save and close the file.**

### Step 7: Start Frontend Server

```powershell
# Start development server
npm run dev
```

**Expected output:**
```
  VITE v7.x.x  ready in xxx ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
```

**✅ Frontend is running!**

---

### Step 8: Access the Application

1. Open your web browser
2. Go to: **http://localhost:5173**
3. You should see the login page

---

## 🧪 TESTING THE APPLICATION

### 1. Register Account
- Click "Register here"
- Fill in: Name, Email, Password (min 6 chars)
- Click "Register"
- You'll be redirected to login

### 2. Login
- Enter email and password
- Click "Login"
- You'll see the Projects dashboard

### 3. Create Project
- Click "Create New Project"
- **Step 1:** Title, Description, Document Type (Word/PowerPoint)
- **Step 2:** Enter topic (e.g., "Market analysis of electric vehicles")
- **Step 3:** 
  - **Word:** Add sections or click "✨ AI Suggest Outline"
  - **PowerPoint:** Enter number of slides and titles
- Click "Create Project"

### 4. Generate Content
- Click "Open" on your project
- Click "Generate Content"
- Wait 30-60 seconds for AI to generate content

### 5. Refine & Export
- Use refinement prompts to improve content
- Click Like/Dislike for feedback
- Add comments
- Click "Export DOCX" or "Export PPTX" to download

---

## 🚀 DEPLOYMENT TO PRODUCTION

### Option 1: Deploy to Render (Backend) + Vercel (Frontend)

#### Backend Deployment on Render

1. **Create Render Account**
   - Go to [render.com](https://render.com)
   - Sign up (free tier available)

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the repository

3. **Configure Settings**
   - **Name:** `ai-doc-generator-backend`
   - **Environment:** `Python 3`
   - **Build Command:**
     ```bash
     cd backend && pip install -r requirements.txt
     ```
   - **Start Command:**
     ```bash
     cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
     ```

4. **Add Environment Variables**
   Click "Environment" tab and add:
   ```
   JWT_SECRET=your-production-secret-key-here
   JWT_ALGO=HS256
   GEMINI_API_KEY=your-gemini-api-key
   DATABASE_URL=sqlite:///./database.db
   ```

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (5-10 minutes)
   - Note your service URL: `https://your-app.onrender.com`

6. **Initialize Database**
   - Go to "Shell" in Render dashboard
   - Run: `cd backend && python init_database.py`

#### Frontend Deployment on Vercel

1. **Install Vercel CLI**
   ```powershell
   npm install -g vercel
   ```

2. **Login to Vercel**
   ```powershell
   vercel login
   ```

3. **Deploy from Frontend Directory**
   ```powershell
   cd frontend
   vercel
   ```

4. **Follow Prompts**
   - Link to existing project or create new
   - Confirm settings
   - Wait for deployment

5. **Add Environment Variable**
   - Go to Vercel Dashboard → Your Project → Settings → Environment Variables
   - Add:
     ```
     VITE_API_URL=https://your-backend.onrender.com
     ```
   - Replace with your actual Render backend URL

6. **Redeploy**
   - Go to Deployments tab
   - Click "Redeploy" on latest deployment

**✅ Your app is now live!**

---

### Option 2: Deploy to Render (Both Backend & Frontend)

#### Backend (Same as above)

#### Frontend on Render

1. **Create Static Site**
   - Click "New +" → "Static Site"
   - Connect GitHub repository

2. **Configure**
   - **Root Directory:** `frontend`
   - **Build Command:** `npm install && npm run build`
   - **Publish Directory:** `frontend/dist`

3. **Add Environment Variable**
   ```
   VITE_API_URL=https://your-backend.onrender.com
   ```

4. **Deploy**
   - Click "Create Static Site"
   - Wait for deployment

---

### Option 3: Deploy to Railway (All-in-One)

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Deploy Backend**
   - Add service → Select backend folder
   - Set start command: `cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Add environment variables (same as Render)

4. **Deploy Frontend**
   - Add service → Select frontend folder
   - Set build command: `npm install && npm run build`
   - Add environment variable: `VITE_API_URL` (use backend Railway URL)

---

## 🔧 TROUBLESHOOTING

### Backend Issues

**Error: "ModuleNotFoundError: No module named 'app'"**
```powershell
# Solution: Make sure you're in backend directory
cd backend
.\venv\Scripts\Activate.ps1
uvicorn app.main:app --reload
```

**Error: "Port 8000 already in use"**
```powershell
# Find and kill process
netstat -ano | findstr :8000
taskkill /PID <process_id> /F

# Or use different port
uvicorn app.main:app --reload --port 8001
```

**Error: "GEMINI_API_KEY not set"**
- Check `.env` file exists in `backend/` directory
- Verify the key is correct (no extra spaces)
- Restart the server after creating/updating .env

**Error: "Database locked"**
```powershell
# Close all terminals using the database
# Delete and reinitialize
del database.db
python init_database.py
```

### Frontend Issues

**Error: "Cannot find module"**
```powershell
cd frontend
Remove-Item -Recurse -Force node_modules
npm install
```

**Error: "API connection failed"**
- Verify backend is running on port 8000
- Check `VITE_API_URL` in frontend `.env` file
- Check browser console for CORS errors
- Verify backend CORS settings include your frontend URL

**Error: "Port 5173 already in use"**
- Vite will automatically use next available port
- Or change port in `vite.config.js`

### Deployment Issues

**Render: Build fails**
- Check `requirements.txt` is correct
- Verify Python version (should be 3.8+)
- Check build logs in Render dashboard

**Vercel: Build fails**
- Check Node.js version (should be 16+)
- Verify `package.json` is correct
- Check build logs in Vercel dashboard

**CORS errors in production**
- Update CORS origins in `backend/app/main.py`:
  ```python
  allow_origins=[
      "http://localhost:5173",
      "https://your-frontend.vercel.app",  # Add your frontend URL
  ],
  ```
- Redeploy backend after changes

---

## 📝 QUICK COMMAND REFERENCE

### Backend
```powershell
cd backend
.\venv\Scripts\Activate.ps1
python init_database.py
uvicorn app.main:app --reload
```

### Frontend
```powershell
cd frontend
npm install
npm run dev
```

### Stop Servers
- Press `CTRL + C` in terminal

---

## ✅ DEPLOYMENT CHECKLIST

Before deploying:

- [ ] All environment variables set
- [ ] Database initialized
- [ ] Backend runs locally without errors
- [ ] Frontend runs locally without errors
- [ ] All features tested
- [ ] CORS settings updated for production URLs
- [ ] API keys are valid
- [ ] GitHub repository is up to date

---

## 🌐 POST-DEPLOYMENT

After deployment:

1. **Test Production URLs**
   - Backend: `https://your-backend.onrender.com/docs`
   - Frontend: `https://your-frontend.vercel.app`

2. **Update CORS** (if needed)
   - Add frontend URL to backend CORS origins
   - Redeploy backend

3. **Monitor**
   - Check Render/Vercel logs
   - Monitor API usage
   - Check for errors

---

## 📚 ADDITIONAL RESOURCES

- **Full Documentation:** See `README.md`
- **Step-by-Step Setup:** See `STEP_BY_STEP_GUIDE.md`
- **Error Fixes:** See `ERRORS_FIXED.md`

---

**🎉 Congratulations! Your application is now deployed and ready to use!**

