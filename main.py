import os

from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from telepot.utils import generate_sign
from tasks import send_mssg
from kombu.exceptions import KombuError

load_dotenv()

app = FastAPI()


users = {
    "loki": os.getenv("CHAT_ID"),
}
secret_key = os.getenv("SECRET_KEY")


@app.get("/message/{user_name}")
async def message_user(user_name: str, message: str, secret: str):
    sign = generate_sign(secret_key, user_name, message=message)
    if sign != secret:
        raise HTTPException(status_code=403, detail="You shall not pass")
    user_id = users.get(user_name)
    try:
        task = send_mssg.apply_async(args=[user_id, message])
    except KombuError:
        return {"status": "failed", "error": "cant schedule message"}
    return {"status": "success", "task_id": task.id}
