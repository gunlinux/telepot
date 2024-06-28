import os

from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from tele import Telepot
from utils import generate_sign

load_dotenv()

app = FastAPI()

telepotApi: Telepot = Telepot(token=os.getenv("TELEGRAM_TOKEN"))

users = {
    "loki": os.getenv("CHAT_ID"),
}
secret_key = os.getenv('SECRET_KEY')


@app.get("/message/{user_name}")
async def message_user(user_name: str, message: str, secret: str):
    sign = generate_sign(secret_key, user_name, message=message)
    if sign != secret:
        raise HTTPException(status_code=403, detail="You shall not pass")
    user_id = users.get(user_name)
    message = telepotApi.send_mssg(chat_id=user_id, message=message)
    return {"status": message}
