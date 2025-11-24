from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .database import SessionLocal
from .models import Project, User
from .schemas import ProjectCreate, ProjectUpdate, ProjectResponse
from .auth.routes import get_current_user

router = APIRouter(prefix="/projects", tags=["Projects"])


# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------
# Create Project (ONLY for logged-in user)
# ---------------------------------------------------
@router.post("/", response_model=ProjectResponse)
def create_project(
    data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = Project(
        title=data.title,
        description=data.description,
        doc_type=data.doc_type,
        topic=data.topic,
        outline=data.outline or [],
        content=data.content or {},
        refinement_history=data.refinement_history or [],
        feedback=data.feedback or {},
        user_id=current_user.id
    )

    db.add(project)
    db.commit()
    db.refresh(project)
    return project


# ---------------------------------------------------
# Get all projects of logged-in user
# ---------------------------------------------------
@router.get("/", response_model=list[ProjectResponse])
def get_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Project).filter(Project.user_id == current_user.id).all()


# ---------------------------------------------------
# Get single project
# ---------------------------------------------------
@router.get("/{project_id}", response_model=ProjectResponse)
def get_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == current_user.id)
        .first()
    )

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


# ---------------------------------------------------
# Update Project
# ---------------------------------------------------
@router.put("/{project_id}", response_model=ProjectResponse)
def update_project(
    project_id: int,
    data: ProjectUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == current_user.id)
        .first()
    )

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if data.title is not None:
        project.title = data.title

    if data.doc_type is not None:
        project.doc_type = data.doc_type

    if data.topic is not None:
        project.topic = data.topic

    if data.outline is not None:
        project.outline = data.outline

    if data.content is not None:
        project.content = data.content

    if data.refinement_history is not None:
        project.refinement_history = data.refinement_history

    if data.feedback is not None:
        project.feedback = data.feedback

    if data.description is not None:
        project.description = data.description

    db.commit()
    db.refresh(project)
    return project


# ---------------------------------------------------
# Delete Project
# ---------------------------------------------------
@router.delete("/{project_id}")
def delete_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = (
        db.query(Project)
        .filter(Project.id == project_id, Project.user_id == current_user.id)
        .first()
    )

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    db.delete(project)
    db.commit()
    return {"message": "Project deleted successfully"}
