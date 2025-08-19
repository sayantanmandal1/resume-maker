from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Any
from datetime import datetime

class UserBase(BaseModel):
    email: EmailStr
    name: Optional[str]

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    class Config:
        orm_mode = True

class Template(BaseModel):
    id: str
    slug: str
    name: str
    thumbnail_url: str
    fields_schema: Any

class ResumeBase(BaseModel):
    title: str
    template_id: str

class ResumeCreate(ResumeBase):
    pass

class Resume(ResumeBase):
    id: int
    user_id: int
    current_version_id: Optional[int]
    created_at: datetime
    updated_at: datetime
    is_shared: bool
    share_token: Optional[str]
    class Config:
        orm_mode = True

class ResumeVersion(BaseModel):
    id: int
    resume_id: int
    version_no: int
    data: Any
    latex_source: str
    pdf_path: Optional[str]
    created_at: datetime
    class Config:
        orm_mode = True

class Collaborator(BaseModel):
    id: int
    resume_id: int
    email: str
    role: str
    invited_at: datetime
    accepted_at: Optional[datetime]
    class Config:
        orm_mode = True

class JobDescription(BaseModel):
    id: int
    resume_id: int
    title: str
    company: Optional[str]
    jd_text: str
    created_at: datetime
    class Config:
        orm_mode = True

class ATSReport(BaseModel):
    id: int
    resume_id: int
    jd_id: int
    score: int
    missing_keywords: Any
    suggestions: Any
    created_at: datetime
    class Config:
        orm_mode = True

class Import(BaseModel):
    id: int
    user_id: int
    source: str
    raw: Any
    normalized: Any
    created_at: datetime
    class Config:
        orm_mode = True

