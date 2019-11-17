import glob
import os
from main_query import rebuild_expression
from query_parser import QueryParser


def list_of_tokens(file_name):
    with open(file_name, encoding="utf-8", errors="ignore") as file:
        file_text = file.read()
        return file_text.split()


def inverted_index():
    path_name = os.path.dirname(os.path.abspath(__file__)) + "/output/"
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


d = inverted_index()
parser = QueryParser("(japan AND zambia) OR western")
tree = parser.parse()
query, files = rebuild_expression(tree,d)

for file in files:
    print(file)