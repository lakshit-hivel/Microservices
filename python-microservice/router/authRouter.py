from sys import prefix
from fastapi import APIRouter, Depends, HTTPException
import schemas, models
from Services import authService
from sqlalchemy.orm import Session
from database import get_db, engine

router = APIRouter(prefix="/auth")

@router.post("/register")
def register_user(user:schemas.AuthUserCreate, db: Session = Depends(get_db)):
    res = authService.create_auth_user(db, user)
    return res

@router.post("/login")
def login_user(user:schemas.AuthUserLogin, db: Session = Depends(get_db)):
    res = authService.login_user(db, user)
    return res
