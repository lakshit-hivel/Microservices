from sys import prefix
from fastapi import APIRouter, Depends, HTTPException
import schemas, models
from Services import userService
from sqlalchemy.orm import Session
from database import get_db, engine

router = APIRouter(prefix="/api")

@router.get("/all-users", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    users = userService.get_all_users(db)
    return users

@router.post("/new-user", response_model=schemas.User)
def create_new_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = userService.create_user(db, user)
    return new_user

@router.get("/get-user/{user_id}", response_model=schemas.User)
def get_user_by_id(user_id:int, db: Session = Depends(get_db)):
    user = userService.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/all-deleted-users", response_model=list[schemas.User])
def get_deleted_users(db: Session = Depends(get_db)):
    deleted_users = userService.get_deleted_users(db)
    return deleted_users

@router.put("/restore-user/{user_id}", response_model=schemas.User)
def restore_deleted_user(user_id:int, db: Session = Depends(get_db)):
    restore_user = userService.restore_user(db, user_id)
    return restore_user

@router.delete("/delete-user/{user_id}", response_model=schemas.User)
def delete_user(user_id:int, db: Session = Depends(get_db)):
    deleted_user = userService.delete_user(db, user_id)
    return deleted_user