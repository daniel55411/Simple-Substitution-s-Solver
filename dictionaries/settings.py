import os


path = os.path.dirname(os.path.abspath(__file__)) + '/lang/'
settings = {
    'en': {
        'ngram_file': path + 'en/english_quadgrams.txt',
        'ngram_file_delimiter': ' ',
        'alphabet': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'ngram_file_encoding': 'utf-8',
        'lang': 'en',
        'PRECENT_GOOD_WORDS': 0.55,
    },
    'ru': {
        'ngram_file': path + 'ru/russian_quadgrams.txt',
        'ngram_file_delimiter': ' ',
        'alphabet': 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ',
        'ngram_file_encoding': 'utf-8',
        'lang': 'ru',
        'PRECENT_GOOD_WORDS': 0.3,
    }
}
