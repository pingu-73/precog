import re
import numpy as np

punctuations = "! ? . , : ; "

def remove_punctuations(docs):
    for i in range(len(docs)):
        for punctuation in punctuations:
            docs[i] = docs[i].replace(punctuation, "")
    return docs


def tokenize(text):
    pattern = re.compile(r'[A-Za-z]+[\w^\']*|[\w^\']*[A-Za-z]+[\w^\']*')
    return pattern.findall(text.lower())


def mapping(tokens):
    word_to_id = {}
    id_to_word = {}
    
    for i, token in enumerate(set(tokens)):
        word_to_id[token] = i
        id_to_word[i] = token
    
    return word_to_id, id_to_word