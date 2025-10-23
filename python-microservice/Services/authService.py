from sqlalchemy.orm import Session
from models import AuthUser
from schemas import AuthUserCreate, AuthUserLogin
from auth.hash_handler import hash_password, verify_password
from auth.jwt_handler import create_access_token
from fastapi import HTTPException

def create_auth_user(db:Session, auth_user:AuthUserCreate):
    hashed_pw = hash_password(auth_user.password)
    new_user = AuthUser(email=auth_user.email, username=auth_user.username, password=hashed_pw)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_access_token({"id": new_user.id, "username": new_user.username})
    return {"message": "User created successfully", "token": token}

def login_user(db:Session, auth_user:AuthUserLogin):
    user = db.query(AuthUser).filter(AuthUser.username == auth_user.username).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    if not verify_password(auth_user.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"id": user.id, "username": user.username})
    return {"message": "User logged in successfully", "token": token}