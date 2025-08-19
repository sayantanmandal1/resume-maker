from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .schemas import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    # TODO: Implement JWT decode and user lookup
    # For now, return a fake user
    return User(id=1, email="test@example.com", name="Test User", created_at=None)

