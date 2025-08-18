from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text, JSON
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    name = Column(String)
    password_hash = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    resumes = relationship('Resume', back_populates='user')

class Template(Base):
    __tablename__ = 'templates'
    id = Column(String, primary_key=True)
    slug = Column(String, unique=True)
    name = Column(String)
    thumbnail_url = Column(String)
    tex_path = Column(String)
    fields_schema = Column(JSON)

class Resume(Base):
    __tablename__ = 'resumes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    template_id = Column(String, ForeignKey('templates.id'))
    current_version_id = Column(Integer, ForeignKey('resume_versions.id'), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    is_shared = Column(Boolean, default=False)
    share_token = Column(String, unique=True, nullable=True)
    user = relationship('User', back_populates='resumes')
    template = relationship('Template')
    versions = relationship('ResumeVersion', back_populates='resume')
    collaborators = relationship('Collaborator', back_populates='resume')

class ResumeVersion(Base):
    __tablename__ = 'resume_versions'
    id = Column(Integer, primary_key=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    version_no = Column(Integer)
    data = Column(JSON)
    latex_source = Column(Text)
    pdf_path = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    resume = relationship('Resume', back_populates='versions')

class Collaborator(Base):
    __tablename__ = 'collaborators'
    id = Column(Integer, primary_key=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    email = Column(String)
    role = Column(String)  # viewer, commenter, editor
    invited_at = Column(DateTime, server_default=func.now())
    accepted_at = Column(DateTime, nullable=True)
    resume = relationship('Resume', back_populates='collaborators')

class JobDescription(Base):
    __tablename__ = 'job_descriptions'
    id = Column(Integer, primary_key=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    title = Column(String)
    company = Column(String)
    jd_text = Column(Text)
    created_at = Column(DateTime, server_default=func.now())

class ATSReport(Base):
    __tablename__ = 'ats_reports'
    id = Column(Integer, primary_key=True)
    resume_id = Column(Integer, ForeignKey('resumes.id'))
    jd_id = Column(Integer, ForeignKey('job_descriptions.id'))
    score = Column(Integer)
    missing_keywords = Column(JSON)
    suggestions = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())

class Import(Base):
    __tablename__ = 'imports'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    source = Column(String)  # linkedin, github, file
    raw = Column(JSON)
    normalized = Column(JSON)
    created_at = Column(DateTime, server_default=func.now())
