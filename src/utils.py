import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import List


def tokenize(text) -> List[str]:
    lemmatizer = WordNetLemmatizer()
    tokens = []
    text = text.lower()
    for sent in nltk.sent_tokenize(text, language="english"):
        for word in nltk.word_tokenize(sent, language="english"):
            word = lemmatizer.lemmatize(word)
            tokens.append(word)
    return tokens
