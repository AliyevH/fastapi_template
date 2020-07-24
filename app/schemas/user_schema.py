from typing import List, Optional
from pydantic import BaseModel, EmailStr
import uuid


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: uuid.UUID

