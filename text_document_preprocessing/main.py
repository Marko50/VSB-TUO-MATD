import sys, getopt
from io_text import read_text
from reuter import preprocess_reuter

file_name = getopt.getopt(sys.argv[1:],"")[1][0]
read_text(file_name, preprocess_reuter)