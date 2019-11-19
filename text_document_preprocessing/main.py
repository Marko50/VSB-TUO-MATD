import sys, getopt

from io_auxiliar.io_text import read_text
from reuter.reuter import preprocess_reuter
from inverted_index.inverted_index import inverted_index
from query.query_parser import QueryParser
from query.rebuild_expression import rebuild_expression


file_name = getopt.getopt(sys.argv[1:],"")[1][0]
query = getopt.getopt(sys.argv[1:],"")[1][1]

#read_text(file_name, preprocess_reuter)

d = inverted_index()
parser = QueryParser(query)
tree = parser.parse()
_query, files = rebuild_expression(tree,d)

for file in files:
    print(file)