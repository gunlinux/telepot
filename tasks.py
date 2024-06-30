import os


from dotenv import load_dotenv
from celery import Celery
from telepot.tele import Telepot

app = Celery('telepot', broker='redis://localhost:6379/0')
load_dotenv()


@app.task
def send_mssg(chat_id, message):
    telepotApi: Telepot = Telepot(token=os.getenv("TELEGRAM_TOKEN"))
    token = os.getenv('TELEGRAM_TOKEN')
    message = telepotApi.send_mssg(chat_id=chat_id, message=message)
