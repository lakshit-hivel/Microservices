from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    email: str
    age: int
    university: str
    company: str
    title: str
    department: str
    address: str
    state: str
    city: str
    phone: str
    country: str = "India"
    gender: str
    profilePicture: str
    role: str = "user"
    isDeleted: bool = False

class UserCreate(UserBase):
    pass

class UserDelete(BaseModel):
    id: int
    isDeleted: bool = True

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# Response schemas with message and data
class UserResponse(BaseModel):
    message: str
    data: User

class UserListResponse(BaseModel):
    message: str
    data: list[User]


class AuthUserBase(BaseModel):
    email: str
    username: str

class AuthUserCreate(AuthUserBase):
    password: str

class AuthUserLogin(BaseModel):
    username: str
    password: str

class AuthUserGet(AuthUserBase):
    id: int
    createdAt: datetime
    updatedAt: datetime

    class Config:
        from_attributes = True
