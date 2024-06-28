import os

from fastapi import FastAPI
from dotenv import load_dotenv
from tele import Telepot

load_dotenv()

app = FastAPI()

telepotApi: Telepot = Telepot(token=os.getenv("TELEGRAM_TOKEN"))

users = {
    "loki": os.getenv("CHAT_ID"),
}


@app.get("/message/{user_name}")
async def message_user(user_name: str, message: str, secret: str = ""):
    user_id = users.get(user_name)
    message = telepotApi.send_mssg(chat_id=user_id, message=message)
    return {"status": message}
