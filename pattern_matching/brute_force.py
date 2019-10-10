# Brute force algorithm for pattern matching

import sys, getopt, time

def brute_force(text, pattern):
    i = 0
    while i < len(text) - len(pattern):
        j = 0
        while j < len(pattern):
            #print("Comparing " + text[i + j] + " with " + pattern[j])
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == len(pattern):
            print("Match found at " + str(i))
        i += 1

pattern = getopt.getopt(sys.argv[1:],"")[1][0]
file = getopt.getopt(sys.argv[1:],"")[1][1]

with open(file, encoding="utf8", errors='ignore') as f:
    file_text = f.read()
# unicoded_text = file_text.decode("utf-8")
    start = time.time()
    brute_force(file_text, pattern)
    end = time.time()
    print("Elapsed time was: " + str(end - start) + " seconds")
    f.close()