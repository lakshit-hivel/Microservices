# models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False)
    university = Column(String, nullable=False)
    company = Column(String, nullable=False)
    title = Column(String, nullable=False)
    department = Column(String, nullable=False)
    address = Column(String, nullable=False)
    state = Column(String, nullable=False)
    city = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    country = Column(String, nullable=False, default="India")
    gender = Column(String, nullable=False)
    profilePicture = Column(String, nullable=False)
    role = Column(String, nullable=False, default="user")
    isDeleted = Column(Boolean, nullable=False, default=False)
    deletedAt = Column(DateTime, nullable=True)
    createdAt = Column(DateTime, default=datetime.utcnow, nullable=False)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class AuthUser(Base):
    __tablename__ = "authUser"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow, nullable=False)
    updatedAt = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
