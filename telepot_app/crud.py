from sqlalchemy.orm import Session

from . import schemas
from telepot_app.models.user import User


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_name(db: Session, name: str):
    return db.query(User).filter(User.name == name).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(name=user.name, chat_id=user.chat_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
