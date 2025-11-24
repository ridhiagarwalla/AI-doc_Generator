# Deployment Guide

## Backend Deployment on Render

### Step 1: Prepare Your Repository
1. Ensure all code is committed and pushed to GitHub
2. Make sure `requirements.txt` is in the `backend/` directory
3. Verify `app/main.py` exists and is the entry point

### Step 2: Create Render Web Service
1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select the repository and branch

### Step 3: Configure Build Settings
- **Name**: `ai-doc-generator-backend` (or your preferred name)
- **Environment**: `Python 3`
- **Build Command**: 
  ```bash
  cd backend && pip install -r requirements.txt
  ```
- **Start Command**: 
  ```bash
  cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT
  ```

### Step 4: Add Environment Variables
In the Render dashboard, go to "Environment" section and add:

```
JWT_SECRET=your-strong-random-secret-key-here
JWT_ALGO=HS256
GEMINI_API_KEY=your-gemini-api-key
DATABASE_URL=sqlite:///./database.db
```

**Note**: For production, consider using PostgreSQL:
1. Create a PostgreSQL database on Render
2. Use the provided connection string for `DATABASE_URL`

### Step 5: Deploy
1. Click "Create Web Service"
2. Wait for deployment to complete
3. Note your service URL (e.g., `https://ai-doc-generator.onrender.com`)

### Step 6: Initialize Database
After first deployment, you may need to initialize the database:
1. Go to "Shell" in Render dashboard
2. Run: `cd backend && python -m app.init_db`

---

## Frontend Deployment on Vercel

### Step 1: Install Vercel CLI (Optional)
```bash
npm i -g vercel
```

### Step 2: Deploy via CLI
1. Navigate to frontend directory:
   ```bash
   cd frontend
   ```

2. Login to Vercel:
   ```bash
   vercel login
   ```

3. Deploy:
   ```bash
   vercel
   ```

4. Follow the prompts:
   - Link to existing project or create new
   - Confirm settings

### Alternative: Deploy via Vercel Dashboard
1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click "Add New Project"
3. Import your GitHub repository
4. Configure:
   - **Framework Preset**: Vite
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`

### Step 3: Add Environment Variables
In Vercel dashboard → Project Settings → Environment Variables:

```
VITE_API_URL=https://your-backend.onrender.com
```

**Important**: Replace `your-backend.onrender.com` with your actual Render backend URL

### Step 4: Redeploy
After adding environment variables, trigger a new deployment:
- Via CLI: `vercel --prod`
- Via Dashboard: Go to Deployments → Redeploy

---

## Frontend Deployment on Netlify

### Step 1: Build Locally (Optional)
```bash
cd frontend
npm run build
```

### Step 2: Deploy via Netlify Dashboard
1. Go to [Netlify Dashboard](https://app.netlify.com)
2. Drag and drop the `frontend/dist` folder
3. Or connect GitHub repository

### Step 3: Configure Build Settings
If connecting via GitHub:
- **Base directory**: `frontend`
- **Build command**: `npm run build`
- **Publish directory**: `frontend/dist`

### Step 4: Add Environment Variables
In Netlify → Site Settings → Environment Variables:

```
VITE_API_URL=https://your-backend.onrender.com
```

### Step 5: Deploy
Netlify will automatically deploy on every push to your repository.

---

## Post-Deployment Checklist

### Backend
- [ ] Verify API is accessible at your Render URL
- [ ] Check API docs at `https://your-backend.onrender.com/docs`
- [ ] Test authentication endpoints
- [ ] Verify database is initialized
- [ ] Check logs for any errors

### Frontend
- [ ] Verify frontend is accessible
- [ ] Test login/registration
- [ ] Verify API calls are working (check browser console)
- [ ] Test document generation
- [ ] Test export functionality

### CORS Configuration
If you encounter CORS errors, update `backend/app/main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://your-frontend.vercel.app",  # Add your frontend URL
        "https://your-frontend.netlify.app",  # Add your frontend URL
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Troubleshooting

### Backend Issues

**Issue**: Build fails
- **Solution**: Check `requirements.txt` is correct and all dependencies are listed

**Issue**: Database errors
- **Solution**: Ensure database is initialized. Run `python -m app.init_db` in Render shell

**Issue**: Gemini API errors
- **Solution**: Verify `GEMINI_API_KEY` is set correctly and has quota remaining

### Frontend Issues

**Issue**: API calls fail
- **Solution**: 
  1. Check `VITE_API_URL` environment variable
  2. Verify backend is running and accessible
  3. Check CORS configuration

**Issue**: Build fails
- **Solution**: 
  1. Check Node.js version (should be 16+)
  2. Delete `node_modules` and reinstall
  3. Check for syntax errors

**Issue**: Environment variables not working
- **Solution**: 
  1. Ensure variables start with `VITE_` prefix
  2. Rebuild and redeploy after adding variables

---

## Production Recommendations

1. **Use PostgreSQL** instead of SQLite for production
2. **Enable HTTPS** (automatic on Render/Vercel/Netlify)
3. **Set up monitoring** (Render/Vercel provide built-in monitoring)
4. **Implement rate limiting** for API endpoints
5. **Add error tracking** (e.g., Sentry)
6. **Set up CI/CD** for automated deployments
7. **Use environment-specific configurations**

---

## Cost Estimates

### Render (Backend)
- **Free Tier**: 750 hours/month
- **Starter Plan**: $7/month (unlimited hours)

### Vercel (Frontend)
- **Free Tier**: Unlimited deployments
- **Pro Plan**: $20/month (for team features)

### Netlify (Frontend)
- **Free Tier**: 100GB bandwidth/month
- **Pro Plan**: $19/month

### Gemini API
- **Free Tier**: 15 requests/minute
- **Paid**: Pay-as-you-go pricing

---

**Note**: Always test your deployment in a staging environment before going to production!

