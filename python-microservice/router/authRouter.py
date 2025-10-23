from sys import prefix
from fastapi import APIRouter, Depends, HTTPException
import schemas, models
from Services import authService
from sqlalchemy.orm import Session
from database import get_db, engine
from auth.jwt_handler import verify_access_token
from fastapi.security import OAuth2PasswordBearer

router = APIRouter(prefix="/auth/login")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@router.post("/register")
def register_user(user:schemas.AuthUserCreate, db: Session = Depends(get_db)):
    res = authService.create_auth_user(db, user)
    return res

@router.post("/login")
def login_user(user:schemas.AuthUserLogin, db: Session = Depends(get_db)):
    res = authService.login_user(db, user)
    return res


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = db.query(models.AuthUser).filter(models.AuthUser.id == payload.get("id")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
