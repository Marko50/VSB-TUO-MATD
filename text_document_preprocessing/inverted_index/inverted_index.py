import glob
import os


def list_of_tokens(file_name):
    with open(file_name, encoding="utf-8", errors="ignore") as file:
        file_text = file.read()
        return file_text.split()


def inverted_index():
    path_name = os.path.dirname(os.path.abspath(__file__)) + "/../output/"
    files = [f for f in glob.glob(path_name + "*.txt", recursive=False)]

    dictionary = dict()
    for file in files:
        dictionary = append_dictionary(dictionary, file)

    return dictionary


def append_dictionary(dictionary, file):
    tokens = list_of_tokens(file)
    for token in tokens:
        if dictionary.get(token):
            dictionary[token].append(file)
        else:
            dictionary[token] = [file]

    return dictionary