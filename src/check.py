"""
This file includes stuff actual checking
"""
from typing import List
from math import log10 as log


class PlagiarismCheck:
    def __init__(self, index: Index, query_path: str):
        self.index = index
        self.query_path = query_path

    # Returns score of query file, matching with each training file
    def find_score(self) -> List[float]:
        score_list = list()
        total_docs = self.index.term_frequency.size()
        tokens = utils.get_tokens(self.query_path)
        for tf_map in self.index.term_frequency:
            score = 0.0
            for token in tokens:
                if token in tf_map:
                    term_weight = 1.0 + log(tf_map[token])
                    doc_freq_weight = log(total_docs / self.index.doc_frequency[token])
                    score += term_weight * doc_freq_weight
            score_list.append(score)
        return score_list
