import httpx


class Telepot:

    def __init__(self, token):
        self.token = token

    def send_mssg(self, chat_id, message):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage'
        params = {
            'chat_id': chat_id,
            'text': message,
        }
        r = httpx.post(url=url, params=params)
        return r.status_code
