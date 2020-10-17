from collections import Counter, defaultdict
from pathlib import Path
from math import log10

from utils import tokenize, normalize


class Index:
    """
    The index which will be used by the PlagiarismChecker as the basis for plagiarism marking
    """

    def __init__(self):
        self.term_freqs = {}
        self.doc_freq = defaultdict(int)

    def add_doc(self, doc_name: Path, doc_contents: str):
        """
        Add the document to the index
        :param doc_name: The name of the document
        :param doc_contents: The contents of the document
        :return: None
        """
        tokens = Counter(tokenize(doc_contents))
        self.term_freqs[doc_name] = tokens
        for token in tokens:
            self.doc_freq[token] += 1

    def normalize_docs(self):
        """
        Apply Cosine Normalization to each doc in the corpus
        :param: None
        :return: None
        """
        total_docs = float(len(self.term_freqs))  # Float conversion for float division in log10(total_docs/count)
        new_doc_freq = {}
        for token, count in self.doc_freq.items():
            new_doc_freq[token] = log10(total_docs / count)
        self.doc_freq = new_doc_freq
        for doc, tf_map in self.term_freqs.items():
            self.term_freqs[doc] = normalize(tf_map, self.doc_freq)
