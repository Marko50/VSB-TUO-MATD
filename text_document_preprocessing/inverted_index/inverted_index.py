import glob
import os
from collections import Counter


def list_of_tokens(file_name):
    with open(file_name, encoding="utf-8", errors="ignore") as file:
        file_text = file.read()
        return set(file_text.split())


def inverted_index():
    path_name = os.path.dirname(os.path.abspath(__file__)) + "/../output/"
    files = [f for f in glob.glob(path_name + "*.txt", recursive=False)]

    inv_index = dict()
    term_freq = dict()
    doc_id = 1
    for file in files:
        tokens = list_of_tokens(file)
        inv_index = append_dictionary(inv_index, tokens, doc_id)
        term_freq = term_frequency(term_freq, tokens, doc_id)
        doc_id += 1

    return inv_index, term_freq


def append_dictionary(dictionary, tokens, doc_id):
    for token in tokens:
        if dictionary.get(token):
            dictionary[token].append(doc_id)
        else:
            dictionary[token] = [doc_id]

    return dictionary

def term_frequency(dictionary, tokens, docID):
    term_frequency = dict(Counter(tokens))
    dictionary[docID] = term_frequency
    return dictionary