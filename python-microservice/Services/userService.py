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
    return db.query(User).all()