from .utils import tokenize
from collections import Counter, defaultdict


class Index:
    def __init__(self):
        self.term_frequencies = {}
        self.doc_frequency = defaultdict(int)

    def add_doc(self, doc_id, text):
        tokens = Counter(tokenize(text))
        self.term_frequencies[doc_id] = tokens
        for token in tokens:
            self.doc_frequency[token] += 1
