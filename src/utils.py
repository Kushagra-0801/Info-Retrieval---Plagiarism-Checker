from collections import Counter
from math import log10, sqrt
from typing import Dict

from nltk.tokenize import sent_tokenize as s_t, word_tokenize as w_t
from nltk.stem import PorterStemmer


def tokenize(text: str) -> Dict[str, int]:
    porter = PorterStemmer()

    """
    for sent in sent_tokenize(text, language="english"):
        for word in word_tokenize(sent, language="english"):
            tokens.append(porter.stem(word))
            
    Faster implementation of the above code
    """
    tokens = [porter.stem(word) for sent in s_t(text, language="english") for word in w_t(sent, language="english")]
    return Counter(tokens)


def normalize(term_freq: Dict[str, int], doc_freq: Dict[str, float]) -> Dict[str, float]:
    new_term_freq = {token: (1 + log10(count)) * doc_freq.get(token, 0.0) for token, count in term_freq.items()}
    l2norm = sqrt(sum(value ** 2 for value in new_term_freq.values()))
    if l2norm != 0.0:
        new_term_freq = {token: value/l2norm for token, value in new_term_freq.items()}
    return new_term_freq
