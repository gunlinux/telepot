from fastapi import FastAPI
from telepot_app.api.routes import message, user
from telepot_app.core.database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(message.router, prefix='/messages', tags=["messages"])
app.include_router(user.router, prefix='/users', tags=["users"])
