from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import telepot_app.schemas as schemas
import telepot_app.crud as crud
from telepot_app.models.user import User
from telepot_app.api.deps import get_db, verify_user_not_exists, get_user_by_id


router = APIRouter()


@router.post("/", response_model=schemas.User)
def create_user(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    valid_user: schemas.UserCreate = Depends(verify_user_not_exists),
):
    return crud.create_user(db=db, user=valid_user)


@router.get("/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=schemas.User)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    existing_user: User = Depends(get_user_by_id),
):
    return existing_user
