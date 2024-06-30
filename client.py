import os
import urllib.parse
import urllib.request

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    print("we can work without python-dotenv")
else:
    load_dotenv()

from telepot.utils import generate_sign


class TelepotClient:
    def __init__(self, host, secret):
        self.base = host
        self.secret = secret

    def send_mssg(self, chat, message):
        url = urllib.parse.urljoin(self.base, f"/messages/{chat}")
        sign = generate_sign(self.secret, chat, message=message)
        params = {
            "message": message,
            "secret": sign,
        }
        query_string = urllib.parse.urlencode(params)
        full_url = f"{url}?{query_string}"
        with urllib.request.urlopen(full_url) as response:
            r = response.read()
            print(r.decode())
        return r


if __name__ == "__main__":
    telepot_client = TelepotClient(
        host=os.getenv("TELEPOT_HOST"), secret=os.getenv("SECRET_KEY")
    )
    telepot_client.send_mssg("loki", "auf")
