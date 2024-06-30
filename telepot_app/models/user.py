from sqlalchemy import Boolean, Column, Integer, String

from telepot_app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    chat_id = Column(String, unique=True, index=True)
    name = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
