import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from typing import List


def preprocess(text) -> List[str]:
    lemmatizer = WordNetLemmatizer()
    tokens = []
    text = text.lower()
    for sent in nltk.sent_tokenize(text, language="english"):
        for words in nltk.word_tokenize(sent, language="english"):
            words = lemmatizer.lemmatize(words)
            if words not in stopwords.words("english"):
                tokens.append(words)
            tokens.append(words)
    return tokens
