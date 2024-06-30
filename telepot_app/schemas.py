from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    chat_id: str


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
