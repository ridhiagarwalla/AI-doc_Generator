from sqlalchemy import Column, Integer, String, ForeignKey, JSON, DateTime, func, Text
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())

    projects = relationship("Project", back_populates="user", cascade="all, delete-orphan")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    title = Column(String, nullable=False)
    doc_type = Column(String, nullable=True)  # "docx" or "pptx"
    topic = Column(Text, nullable=True)  # Main topic/prompt
    outline = Column(JSON, default=[])  # List of sections/slides
    content = Column(JSON, default={})  # Generated content by section/slide
    refinement_history = Column(JSON, default=[])  # History of refinements
    feedback = Column(JSON, default={})  # Like/dislike and comments per section
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    
    description = Column(Text, nullable=True)

    user = relationship("User", back_populates="projects")

class Content(Base):
    __tablename__ = "content"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    section_id = Column(String, nullable=False)
    text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Refinement(Base):
    __tablename__ = "refinements"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    section_id = Column(String, nullable=False)
    prompt = Column(Text, nullable=False)
    updated_text = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=func.now())

