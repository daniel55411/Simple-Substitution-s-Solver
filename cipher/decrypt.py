from cipher.cracker.crack import Cracker


def decrypt(text, settings):
    cracker = Cracker(settings)
    return cracker.crack(text)
