from options import options_parser
from dictionaries.settings import settings
from cipher.encrypt import encrypt
from cipher.decrypt import decrypt
from dictionaries.prepare_dict import prepare
import os


def main():
    options = options_parser().parse_opt()
    alphabet = settings[options.language]['alphabet']
    if options.mode == 'enc':
        result = encrypt(options.input.read(), alphabet)
        options.output.write(result['text'])
    else:
        result = decrypt(options.input.read(), settings[options.language])
        options.output.write(result['text'])
    options.input.close()
    options.output.close()


if __name__ == "__main__":
    main()
