from pydantic import BaseModel, EmailStr
from typing import Optional, Dict, List, Any


# -----------------------
# User Schemas
# -----------------------

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    model_config = {"from_attributes": True}  # Pydantic v2


# -----------------------
# Project Schemas
# -----------------------

class ProjectBase(BaseModel):
    title: str
    description: str | None = None
    doc_type: Optional[str] = None  # "docx" or "pptx"
    topic: Optional[str] = None
    outline: Optional[List[Dict[str, Any]]] = None
    content: Optional[Dict[str, Any]] = None
    refinement_history: Optional[List[Dict[str, Any]]] = None
    feedback: Optional[Dict[str, Any]] = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    title: Optional[str] = None
    description: Optional[str] = None
    doc_type: Optional[str] = None
    topic: Optional[str] = None
    outline: Optional[List[Dict[str, Any]]] = None
    content: Optional[Dict[str, Any]] = None
    refinement_history: Optional[List[Dict[str, Any]]] = None
    feedback: Optional[Dict[str, Any]] = None


class ProjectResponse(ProjectBase):
    id: int
    user_id: int

    model_config = {"from_attributes": True}  # Pydantic v2


# -----------------------
# Document Generation Schemas
# -----------------------

class GenerateContentRequest(BaseModel):
    section_id: str
    prompt: Optional[str] = None


class RefineContentRequest(BaseModel):
    section_id: str
    refinement_prompt: str


class FeedbackRequest(BaseModel):
    section_id: str
    like: Optional[bool] = None
    comment: Optional[str] = None


class AIGenerateOutlineRequest(BaseModel):
    topic: str
    doc_type: str  # "docx" or "pptx"
