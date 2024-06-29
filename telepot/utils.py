import hashlib
import os
import logging

logger = logging.getLogger(__name__)

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    logger.debug("we can work without python-dotenv")
else:
    load_dotenv()


def generate_sign(secret, *args, **kwargs) -> str:
    hash_ = hashlib.sha256()

    for arg in args:
        hash_.update(arg.encode())

    for k, v in kwargs.items():
        hash_.update(k.encode())
        hash_.update(v.encode())

    hash_.update(secret.encode())
    return hash_.hexdigest()


def is_valid(secret, sign, *args, **kwargs) -> bool:
    return generate_sign(secret, *args, **kwargs) == sign


if __name__ == "__main__":
    secret = os.getenv("SECRET_KEY")
    sign = generate_sign(secret, "loki", message="loki_was_here")
    print(sign)
