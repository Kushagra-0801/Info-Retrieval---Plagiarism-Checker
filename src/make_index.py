from collections import Counter, defaultdict
from pathlib import Path

from utils import tokenize


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
