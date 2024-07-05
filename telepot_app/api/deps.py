from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
import telepot_app.schemas as schemas
from telepot_app.core.database import SessionLocal
from telepot_app import crud


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_user_not_exists(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db, name=user.name)
    if db_user:
        raise HTTPException(status_code=400, detail="name already registered")
    return user


def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    return db_user
