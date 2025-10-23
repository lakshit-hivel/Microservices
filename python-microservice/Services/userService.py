from models import User
from sqlalchemy.orm import Session
from schemas import UserCreate, UserDelete, User as UserSchema


def create_user(db:Session, user:UserCreate):
    new_user_instance = User(**user.model_dump())
    db.add(new_user_instance)
    db.commit()
    db.refresh(new_user_instance)
    return new_user_instance

def get_all_users(db:Session):
    return db.query(User).filter(User.isDeleted==False).all()

def get_user_by_id(db:Session, user_id:int):
    return db.query(User).filter(User.id == user_id).first()

def get_deleted_users(db:Session):
    return db.query(User). filter(User.isDeleted==True).all()

def restore_user(db:Session, user_id:int):
    user = db.query(User).filter(User.id == user_id).first()
    user.isDeleted = False
    db.commit()
    db.refresh(user)
    return user

def delete_user(db:Session, user_id:int):
    user = db.query(User).filter(User.id == user_id).first()
    user.isDeleted = True
    db.commit()
    db.refresh(user)
    return user