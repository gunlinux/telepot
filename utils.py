import hashlib
import os
from dotenv import load_dotenv


def generate_sign(secret, *args, **kwargs) -> str:
    hash = hashlib.sha256()

    for arg in args:
        hash.update(arg.encode())

    for k, v in kwargs.items():
        hash.update(k.encode())
        hash.update(v.encode())

    hash.update(secret.encode())
    return hash.hexdigest()


def is_valid(secret, sign, *args, **kwargs) -> bool:
    return generate_sign(secret, *args, **kwargs) == sign


if __name__ == '__main__':
    load_dotenv()
    secret = os.getenv('SECRET_KEY')
    sign = generate_sign(secret, 'loki', message='loki_was_here')
    print(sign)
