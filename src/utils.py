from math import log10, sqrt
from typing import List, Dict

import nltk
from nltk.stem import WordNetLemmatizer


def tokenize(text) -> List[str]:
    lemmatizer = WordNetLemmatizer()
    tokens = []
    text = text.lower()
    for sent in nltk.sent_tokenize(text, language="english"):
        for word in nltk.word_tokenize(sent, language="english"):
            word = lemmatizer.lemmatize(word)
            tokens.append(word)
    return tokens


def normalize(term_freq: Dict[str, int], doc_freq: Dict[str, float]) -> Dict[str, float]:
    l2norm = 0.0
    new_term_freq = {}
    for token, count in term_freq.items():
        new_term_freq[token] = (1 + log10(count)) * doc_freq.get(token, 0.0)
        l2norm += new_term_freq[token] ** 2
    l2norm = sqrt(l2norm)
    if l2norm != 0.0:
        for token in new_term_freq.keys():
            new_term_freq[token] /= l2norm
    return new_term_freq
