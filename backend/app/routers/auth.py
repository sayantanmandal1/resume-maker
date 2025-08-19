from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/auth", tags=["auth"])

class RegisterRequest(BaseModel):
    email: str
    name: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/register")
def register(req: RegisterRequest):
    # TODO: Implement real registration
    return {"msg": "Registered (stub)", "user": {"email": req.email, "name": req.name}}

@router.post("/login")
def login(req: LoginRequest):
    # TODO: Implement real login
    return {"access_token": "fake-jwt-token", "token_type": "bearer"}

