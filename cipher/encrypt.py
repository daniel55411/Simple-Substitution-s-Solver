import random


def encrypt(message, ABC, key=None):
    if key is None:
        key = list(ABC)
        random.shuffle(key)
        key = "".join(key)
    trans = str.maketrans(ABC, key)
    return dict(key=key, text=message.upper().translate(trans))
