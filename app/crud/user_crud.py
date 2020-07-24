from app.crud.base_crud import BaseCrud
from sqlalchemy.orm import Session
from pydantic import EmailStr


class UserCrud(BaseCrud):
    __abstract__ = True

    @classmethod
    def get_by_email(cls, db: Session, email: EmailStr):
        return db.query(cls).filter(cls.email == email).first()

    @classmethod
    def get_by_pin(cls, db: Session, pin: str):
        return db.query(cls).filter(cls.pin == pin).first()