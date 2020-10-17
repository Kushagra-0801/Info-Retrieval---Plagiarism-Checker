from math import log10
from pathlib import Path
from typing import Dict

import utils
from make_index import Index


class PlagiarismChecker:
    """
    Checks files for plagiarism w.r.t to the index given during initialization
    """

    def __init__(self, index: Index):
        self.index = index

    def find_score(self, contents: str) -> Dict[Path, float]:
        """
        Check file contents for plagiarism
        :param contents: The file contents to check for plagiarism
        :return: Dictionary of plagiarism score w.r.t each original document
        """
        score_list = {}
        total_docs = len(self.index.term_freqs)
        tokens = set(utils.tokenize(contents))
        for document, tf_map in self.index.term_freqs.items():
            score = 0.0
            for token in tokens:
                if token in tf_map:
                    term_weight = 1.0 + log10(tf_map[token])
                    doc_freq_weight = log10(total_docs / self.index.doc_freq[token])
                    score += term_weight * doc_freq_weight
            score_list[document] = score
        return score_list
