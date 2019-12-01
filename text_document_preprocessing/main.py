import sys, getopt

from io_auxiliar.io_text import read_text
from reuter.reuter import preprocess_reuter
from inverted_index.inverted_index import inverted_index
from query.query_parser import QueryParser
from query.rebuild_expression import rebuild_expression
from variable_byte_encoding.fibonacci_encoding import fibonacci_variable_byte_encoding
from vector_model.term_frequency import tf_idf_weights


file_name = getopt.getopt(sys.argv[1:],"")[1][0]
query = getopt.getopt(sys.argv[1:],"")[1][1]

#read_text(file_name, preprocess_reuter)

d, term_freq = inverted_index()
tf_idf = tf_idf_weights(d, term_freq)

# size_of_inverted_index = 0
# for _k,v in d.items():
#     size_of_inverted_index += sys.getsizeof(v)
# print("Uncompressed postings size is " + str(size_of_inverted_index) + " bytes.")
# compressed_inverted_index = fibonacci_variable_byte_encoding(d)
# size_of_compressed_inverted_index = 0
# for _k,v in compressed_inverted_index.items():
#     size_of_compressed_inverted_index += sys.getsizeof(v)
# print("Compressed postings size is " + str(size_of_compressed_inverted_index) + " bytes.")

parser = QueryParser(query)
tree = parser.parse()
_query, files = rebuild_expression(tree,d)

terms = query.replace("AND", "").replace("OR", "").replace("NOT","").replace("(","").replace(")","").split("  ")
print(files)
scores = dict()
for term in terms:
    for doc_id in files:
        scores[(term, doc_id)] = tf_idf[(term,doc_id)]

