import re
import random
from cipher.cracker.scoring import Ngram
from cipher.encrypt import encrypt
from dictionaries.prepare_dict import prepare, similar


class Cracker:
    def __init__(self, settings):
        self.score = Ngram(settings).score
        self.ABC = settings['alphabet']
        self.key = list(self.ABC)
        self.maxscore = float('-inf')
        print("Preparing dictionary...")
        self.wordlist = prepare(settings['lang'])
        self.PRECENT_GOOD_WORDS = settings['PRECENT_GOOD_WORDS']
        print("Ok... Dictioanry is ready")

    def crack(self, text):
        words = re.findall('[{}]+'.format(self.ABC), text.upper())[:200]
        encrypted_text = ''.join(words)
        score, key = self.maxscore, self.key[:]
        result_text = ''
        while similar(words, self.wordlist) < self.PRECENT_GOOD_WORDS:
            random.shuffle(key)
            decrypted_text = encrypt(
                encrypted_text, self.ABC, ''.join(key))['text']
            score = self.score(decrypted_text)
            iteration = 0
            while iteration < 1000:
                first = random.randint(0, len(self.ABC) - 1)
                second = random.randint(0, len(self.ABC) - 1)
                key_successor = key[:]
                key_successor[first], key_successor[second] = key_successor[second], key_successor[first]
                decrypted_text = encrypt(
                    encrypted_text, self.ABC, ''.join(key_successor))['text']
                score_successor = self.score(decrypted_text)
                if score_successor > score:
                    score = score_successor
                    key = key_successor[:]
                    iteration = 0
                iteration += 1
            if score > self.maxscore:
                self.maxscore = score
                self.key = key
                result_text = encrypt(
                    text, self.ABC, ''.join(
                        self.key))['text']
                words = re.findall('[{}]+'.format(self.ABC),
                                   result_text.upper())[:200]
                print(
                    'similar with encrypted text: ',
                    similar(
                        words,
                        self.wordlist))
                print('possible key: ' + ''.join(self.key))
                print()
        return {
            'key': ''.join(self.key),
            'text': result_text
        }
