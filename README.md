AI-Assisted Document Authoring & Generation Platform

An end-to-end full-stack web application that lets authenticated users generate, refine, and export business documents using AI (Gemini / DeepSeek / Groq).

Users can:
✅ Create projects
✅ Choose DOCX or PPTX
✅ Define outlines / slide titles
✅ Generate content using AI
✅ Refine each section interactively
✅ Export final .docx / .pptx files
🚀 Features
1. User Authentication

JWT-based login & registration

Secure endpoints

Each user sees ONLY their own projects

2. Project Dashboard

View all created projects

Create new document configurations

3. Document Setup

Select Word (.docx) or PowerPoint (.pptx)

Add, edit, reorder section headers or slide titles

(Optional) AI-Suggest Outline

4. AI-Powered Content Generation

Uses LLM API (Gemini, DeepSeek, or Groq) to generate:

Section-wise content (for Word)

Slide-wise content (for PowerPoint)

5. Interactive Refinement Editor

For each section/slide, users can:

Enter refinement prompts

Like / Dislike previous output

Add comments

Track refinement history

6. Export

Backend assembles a .docx or .pptx

Sends file for download

100% offline formatting using python-docx / python-pptx

🛠️ Tech Stack
Frontend

React + Vite

Axios

React Router

Tailwind CSS / Custom UI

Backend

FastAPI

JWT Authentication

python-docx

python-pptx

LLM Integrations (Gemini / DeepSeek / Groq)

Database

SQLite / PostgreSQL (configurable)

SQLAlchemy ORM

📁 Folder Structure
ai-doc-generator/
│── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── auth/
│   │   ├── projects/
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── database.py
│   │   ├── utils/
│   ├── venv/
│   ├── requirements.txt
│   └── .env

│── frontend/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── api/
│   │   ├── App.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── public/

│── README.md

🔧 Installation & Setup
1. Clone the Repo
git clone https://github.com/your-username/ai-doc-generator.git
cd ai-doc-generator

🖥️ Backend Setup (FastAPI)
2. Create Virtual Environment
cd backend
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux

3. Install Python Dependencies
pip install -r requirements.txt

🔐 Environment Variables (backend/.env)

Create a .env file inside backend/:

SECRET_KEY=your_jwt_secret
ALGORITHM=HS256

# Choose one of these ↓↓↓
GEMINI_API_KEY=your_key_here
DEEPSEEK_API_KEY=your_key_here
GROQ_API_KEY=your_key_here

LLM_PROVIDER=gemini   # or deepseek or groq

▶️ Start Backend Server
uvicorn app.main:app --reload


Backend runs at:
👉 http://127.0.0.1:8000

Swagger docs:
👉 http://127.0.0.1:8000/docs

🖥️ Frontend Setup (React + Vite)
1. Install Node dependencies
cd ../frontend
npm install

2. Create config file

Create: frontend/src/api/config.js

export const API_BASE_URL = "http://127.0.0.1:8000";

3. Run Frontend
npm run dev


Frontend available at:
👉 http://localhost:5173

📦 Build for Production
npm run build

🎥 Demo Video Requirements

Your final submission must include a demo video showing:

✔ User Registration & Login
✔ Create Word document
✔ Create PowerPoint document
✔ AI content generation
✔ Refinement (like/dislike, comments, revise text)
✔ Export DOCX
✔ Export PPTX

📌 API Usage Notes
Gemini API

Google now requires billing enabled to generate a valid key.

DeepSeek API (Recommended Free Option)

No card needed, unlimited free usage.
https://platform.deepseek.com/api_keys

Groq API (Free Fast Llama)

https://console.groq.com/keys

🧪 Future Improvements

Realtime collaboration

Auto-saving

Custom templates

PDF export

Multi-language support
