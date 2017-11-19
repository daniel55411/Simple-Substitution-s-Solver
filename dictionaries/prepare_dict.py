import os
import re


def prepare(lang):
    path = os.path.dirname(os.path.abspath(__file__)) + \
        '/lang/' + lang + '/wordlist/'
    dictionaries = os.listdir(path)
    words = set()
    for file in dictionaries:
        with open(path + file, 'r', encoding='utf-8') as f:
            words.update(map(lambda x: x.upper(), re.findall('\w+', f.read())))

    return words


def similar(words, wordlist):
    return len([i for i in words if i.upper() in wordlist]) / len(words)
