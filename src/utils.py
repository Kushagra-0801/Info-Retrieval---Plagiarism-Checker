from collections import defaultdict
from typing import List, Dict
from math import log10, sqrt

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


def normalize(term_freq: Dict[str, float], doc_freq: defaultdict) -> Dict[str, float]:
    l2norm = 0.0
    for key, value in term_freq.items():
        term_freq[key] = (1 + log10(value)) * doc_freq[key]
        l2norm += pow(term_freq[key], 2)
    l2norm = sqrt(l2norm)
    if l2norm != 0.0:
        for key in term_freq.keys():
            term_freq[key] /= l2norm
    return term_freq
