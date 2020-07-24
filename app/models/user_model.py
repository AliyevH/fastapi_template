from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING
from sqlalchemy.dialects.postgresql import UUID
from app.crud.user_crud import UserCrud


class User(UserCrud):
    __tablename__ = "users"

    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email = Column(String, index=True)
