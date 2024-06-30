from fastapi import FastAPI
from telepot_app.api.routes import message

app = FastAPI()

app.include_router(message.router, prefix='/messages', tags=["messages"])
