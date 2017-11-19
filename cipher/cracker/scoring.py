from math import log10


class Ngram:
    def __init__(self, settings):
        self.settings = settings
        self.count_ngram = 0
        self.n = 0
        self._parse()

    def _parse(self):
        self.ngrams = {}
        for line in open(self.settings['ngram_file'], 'r',
                         encoding=self.settings['ngram_file_encoding']):
            key, count = line.split(self.settings['ngram_file_delimiter'])
            self.ngrams[key] = int(count)
        self.count_ngram = sum(self.ngrams.values())
        self.n = len(key)
        for key in self.ngrams:
            self.ngrams[key] = log10(
                float(
                    self.ngrams[key]) /
                self.count_ngram)
        self.floor = log10(0.01 / self.count_ngram)

    def score(self, text):
        score = 0
        for i in range(len(text) - self.n + 1):
            if text[i: i + self.n] in self.ngrams:
                score += self.ngrams[text[i: i + self.n]]
            else:
                score += self.floor
        return score
