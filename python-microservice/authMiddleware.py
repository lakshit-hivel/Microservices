from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import get_db
from auth.jwt_handler import verify_access_token
import models

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.query(models.AuthUser).filter(models.AuthUser.id == payload.get("id")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
