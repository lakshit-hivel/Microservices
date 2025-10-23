from sys import prefix
from fastapi import APIRouter, Depends, HTTPException, Request
import schemas, models
from Services import userService
from sqlalchemy.orm import Session
from database import get_db, engine
from router import authRouter
from authMiddleware import get_current_user
from rateLimiter import limiter

router = APIRouter(prefix="/api")

@router.get("/all-users", response_model=schemas.UserListResponse)
@limiter.limit("10/minute")
def get_all_users(request: Request,db: Session = Depends(get_db), current_user: models.AuthUser = Depends(get_current_user)):
    
    users = userService.get_all_users(db)
    return {"message": "All users fetched successfully", "data": users}

@router.post("/new-user", response_model=schemas.UserResponse)
@limiter.limit("10/minute")
def create_new_user(request: Request,user:schemas.UserCreate, db: Session = Depends(get_db), current_user: models.AuthUser = Depends(get_current_user)):
    new_user = userService.create_user(db, user)
    return {"message": "User created successfully", "data": new_user}

@router.get("/get-user/{user_id}", response_model=schemas.UserResponse)
@limiter.limit("10/minute")
def get_user_by_id(request: Request,user_id:int, db: Session = Depends(get_db), current_user: models.AuthUser = Depends(get_current_user)):
    user = userService.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User fetched successfully", "data": user}

@router.get("/all-deleted-users", response_model=schemas.UserListResponse)
@limiter.limit("10/minute")
def get_deleted_users(request: Request, db: Session = Depends(get_db), current_user: models.AuthUser = Depends(get_current_user)):
    deleted_users = userService.get_deleted_users(db)
    return {"message": "All deleted users fetched successfully", "data": deleted_users}

@router.put("/restore-user/{user_id}", response_model=schemas.UserResponse)
@limiter.limit("10/minute")
def restore_deleted_user(request: Request, user_id:int, db: Session = Depends(get_db), current_user: models.AuthUser = Depends(get_current_user)):
    restore_user = userService.restore_user(db, user_id)
    return {"message": "User restored successfully", "data": restore_user}

@router.delete("/delete-user/{user_id}", response_model=schemas.UserResponse)
@limiter.limit("10/minute")
def delete_user(request: Request, user_id:int, db: Session = Depends(get_db), current_user: models.AuthUser = Depends(get_current_user)):
    deleted_user = userService.delete_user(db, user_id)
    return {"message": "User deleted successfully", "data": deleted_user}