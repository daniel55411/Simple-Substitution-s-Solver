import sys
sys.path.insert(0, '..')

import unittest
from cipher.encrypt import encrypt
from cipher.decrypt import decrypt
from dictionaries.settings import settings
from dictionaries.prepare_dict import similar
from cipher.cracker.scoring import Ngram


class Test(unittest.TestCase):
    def setUp(self):
        self.ABC = settings['en']['alphabet']
        self.settings = settings['en']
        self.score = Ngram(self.settings).score

    def test_encrypt_with_my_key(self):
        new_ABC = list(self.ABC)
        new_ABC[0], new_ABC[1] = new_ABC[1], new_ABC[0]
        result = encrypt('abc', self.ABC, ''.join(new_ABC))['text']
        self.assertEqual(result, 'BAC')

    def test_encrypt(self):
        result = encrypt('abc', self.ABC)
        expected_result = encrypt(
            result['text'],
            result['key'],
            self.ABC)['text']
        self.assertEqual(expected_result, 'ABC')

    def test_decrypt(self):
        text = open('../examples/test3.txt').read()
        ans = open('../examples/asnwer3.txt').read()
        result = decrypt(text, self.settings)['text']
        self.assertEqual(result, ans)

    def test_occur_similar_success(self):
        words = ['NAME', 'THINK', 'ABOUT', 'IT', 'MAN', 'EASY', 'REAL', 'TALK']
        wordlist = set(words + ['SOME', 'TEXT'])
        self.assertEqual(similar(words, wordlist), 1.0)
        self.assertTrue(similar(words, wordlist) >
                        self.settings['PRECENT_GOOD_WORDS'])

    def test_occur_similar_fail(self):
        words = ['HFHSAD', 'UASHDAUSD', 'ADASD', 'HELLO']
        wordlist = set(['NAME', 'THINK', 'ABOUT', 'IT', 'MAN',
                        'EASY', 'REAL', 'TALK', 'HELLO'])
        self.assertEqual(similar(words, wordlist), 0.25)
        self.assertFalse(similar(words, wordlist) >
                         self.settings['PRECENT_GOOD_WORDS'])

    def test_ngram_score(self):
        scores = self.score('ATTA')
        self.assertAlmostEqual(scores, -3.929836177225652, 2)


if __name__ == "__main__":
    unittest.main()
