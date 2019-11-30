import glob
import os


def list_of_tokens(file_name):
    with open(file_name, encoding="utf-8", errors="ignore") as file:
        file_text = file.read()
        return set(file_text.split())


def inverted_index():
    path_name = os.path.dirname(os.path.abspath(__file__)) + "/../output/"
    files = [f for f in glob.glob(path_name + "*.txt", recursive=False)]

    dictionary = dict()
    doc_id = 1
    for file in files:
        dictionary = append_dictionary(dictionary, file, doc_id)
        doc_id += 1

    return dictionary


def append_dictionary(dictionary, file, doc_id):
    tokens = list_of_tokens(file)
    for token in tokens:
        if dictionary.get(token):
            dictionary[token].append(doc_id)
        else:
            dictionary[token] = [doc_id]

    return dictionary