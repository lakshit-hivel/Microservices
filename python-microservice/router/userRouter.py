from sys import prefix
from fastapi import APIRouter, Depends, HTTPException
import schemas, models
from Services import userService
from sqlalchemy.orm import Session
from database import get_db, engine

router = APIRouter(prefix="/api")

@router.get("/users", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    users = userService.get_all_users(db)
    return users

@router.post("/users", response_model=schemas.User)
def create_new_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = userService.create_user(db, user)
    return new_user