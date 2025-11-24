# AI-Assisted Document Authoring & Generation Platform

A full-stack web application that allows authenticated users to generate, refine, and export structured business documents (Word .docx and PowerPoint .pptx) using AI-powered content generation.

## 🚀 Features

- **User Authentication**: Secure JWT-based authentication system
- **Project Management**: Create, view, update, and delete projects
- **Document Configuration**: 
  - Word Documents: Create custom outlines with section headers
  - PowerPoint Presentations: Define slides with titles
- **AI Content Generation**: Generate content using Google Gemini API
- **Interactive Refinement**: 
  - Refine content with AI prompts
  - Like/Dislike feedback system
  - Comment system for each section/slide
- **Document Export**: Export final documents as .docx or .pptx files
- **AI-Generated Templates**: Optional AI-suggested outlines

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI
- **Database**: SQLite (via SQLAlchemy ORM)
- **Authentication**: JWT (python-jose)
- **AI Integration**: Google Gemini API
- **Document Generation**: python-docx, python-pptx

### Frontend
- **Framework**: React 19
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Routing**: React Router DOM
- **HTTP Client**: Axios

## 📋 Prerequisites

- Python 3.8+
- Node.js 16+
- npm or yarn
- Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))

## 🔧 Installation & Setup

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Create `.env` file**:
   ```bash
   cp .env.example .env
   ```

6. **Update `.env` file** with your configuration:
   ```env
   JWT_SECRET=your-secret-key-change-this-in-production
   JWT_ALGO=HS256
   GEMINI_API_KEY=your-gemini-api-key-here
   DATABASE_URL=sqlite:///./database.db
   ```

7. **Initialize database**:
   ```bash
   python -m app.init_db
   ```

8. **Run the backend server**:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

   The API will be available at `http://localhost:8000`
   API documentation: `http://localhost:8000/docs`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Create `.env` file**:
   ```bash
   cp .env.example .env
   ```

4. **Update `.env` file** (if needed):
   ```env
   VITE_API_URL=http://localhost:8000
   ```

5. **Start development server**:
   ```bash
   npm run dev
   ```

   The frontend will be available at `http://localhost:5173`

## 📖 Usage Guide

### 1. User Registration & Login
- Navigate to the registration page
- Create an account with your email and password
- Login with your credentials

### 2. Create a Project
- Click "Create New Project" on the dashboard
- **Step 1**: Enter project title, description, and select document type (Word or PowerPoint)
- **Step 2**: Enter the main topic/prompt for your document
- **Step 3**: 
  - **For Word**: Add section headers manually or use "AI Suggest Outline"
  - **For PowerPoint**: Enter number of slides and slide titles

### 3. Generate Content
- Open your project
- Click "Generate Content" to generate AI content for all sections/slides
- Wait for the generation to complete

### 4. Refine Content
- For each section/slide:
  - Enter a refinement prompt (e.g., "Make this more formal", "Convert to bullet points")
  - Click "Refine" to update the content
  - Use Like/Dislike buttons to provide feedback
  - Add comments for notes

### 5. Export Document
- Click "Export DOCX" or "Export PPTX" button
- The document will be downloaded automatically

## 🗂️ Project Structure

```
ai-doc-generator/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app entry point
│   │   ├── config.py             # Configuration
│   │   ├── database.py           # Database setup
│   │   ├── models.py             # SQLAlchemy models
│   │   ├── schemas.py            # Pydantic schemas
│   │   ├── init_db.py            # Database initialization
│   │   ├── auth/
│   │   │   ├── routes.py         # Authentication routes
│   │   │   └── utils.py          # Auth utilities
│   │   ├── projects_routes.py    # Project CRUD routes
│   │   ├── document_routes.py    # Document generation & export routes
│   │   └── services/
│   │       └── gemini_service.py # Gemini API integration
│   ├── requirements.txt
│   ├── .env.example
│   └── database.db               # SQLite database (created after init)
│
└── frontend/
    ├── src/
    │   ├── api/
    │   │   └── axios.js          # Axios configuration
    │   ├── components/
    │   │   └── Navbar.jsx        # Navigation component
    │   ├── pages/
    │   │   ├── login.jsx         # Login page
    │   │   ├── Register.jsx     # Registration page
    │   │   ├── Dashboard.jsx     # Projects dashboard
    │   │   ├── CreateProject.jsx # Project creation wizard
    │   │   └── ProjectEditor.jsx # Content editor & refinement
    │   ├── App.jsx               # Main app component
    │   ├── main.jsx              # React entry point
    │   └── index.css             # Global styles
    ├── package.json
    ├── tailwind.config.js
    ├── postcss.config.js
    ├── vite.config.js
    └── .env.example
```

## 🌐 API Endpoints

### Authentication
- `POST /auth/register` - Register new user
- `POST /auth/login` - Login user
- `GET /auth/me` - Get current user (protected)

### Projects
- `GET /projects` - Get all user projects (protected)
- `POST /projects` - Create new project (protected)
- `GET /projects/{id}` - Get project by ID (protected)
- `PUT /projects/{id}` - Update project (protected)
- `DELETE /projects/{id}` - Delete project (protected)

### Document Generation
- `POST /projects/{id}/generate` - Generate content for all sections (protected)
- `POST /projects/{id}/generate_section` - Generate content for single section (protected)
- `POST /projects/{id}/refine` - Refine section content (protected)
- `POST /projects/{id}/feedback` - Submit feedback/comment (protected)
- `POST /projects/{id}/ai-outline` - Generate AI outline (protected)
- `GET /projects/{id}/export/docx` - Export as Word document (protected)
- `GET /projects/{id}/export/pptx` - Export as PowerPoint (protected)

## 🚀 Deployment

### Backend Deployment (Render)

1. **Create a new Web Service** on [Render](https://render.com)

2. **Connect your GitHub repository**

3. **Configure build settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

4. **Add Environment Variables**:
   - `JWT_SECRET`: Your secret key
   - `JWT_ALGO`: HS256
   - `GEMINI_API_KEY`: Your Gemini API key
   - `DATABASE_URL`: sqlite:///./database.db (or use PostgreSQL)

5. **Deploy**

### Frontend Deployment (Vercel)

1. **Install Vercel CLI**:
   ```bash
   npm i -g vercel
   ```

2. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

3. **Deploy**:
   ```bash
   vercel
   ```

4. **Set Environment Variables** in Vercel dashboard:
   - `VITE_API_URL`: Your Render backend URL (e.g., `https://your-backend.onrender.com`)

5. **Redeploy** after setting environment variables

### Alternative: Netlify

1. **Build the project**:
   ```bash
   cd frontend
   npm run build
   ```

2. **Deploy to Netlify**:
   - Drag and drop the `dist` folder to Netlify
   - Or connect GitHub repository

3. **Set Environment Variables**:
   - `VITE_API_URL`: Your backend URL

## 🔒 Security Notes

- Change `JWT_SECRET` to a strong random string in production
- Use environment variables for all sensitive data
- Consider using PostgreSQL instead of SQLite for production
- Implement rate limiting for API endpoints
- Add CORS configuration for production domains only

## 🐛 Troubleshooting

### Backend Issues

1. **Database not found**:
   - Run `python -m app.init_db` to initialize the database

2. **Gemini API errors**:
   - Verify your `GEMINI_API_KEY` is correct
   - Check API quota limits

3. **Import errors**:
   - Ensure virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

### Frontend Issues

1. **API connection errors**:
   - Verify backend is running on port 8000
   - Check `VITE_API_URL` in `.env` file
   - Check CORS settings in backend

2. **Build errors**:
   - Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on the GitHub repository.

---

**Built with ❤️ using FastAPI, React, and Google Gemini API**

#   A I - d o c _ G e n e r a t o r  
 