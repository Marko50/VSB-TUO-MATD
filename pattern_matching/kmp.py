import sys, getopt, time

def preprocessing(pattern):
    kmp_next = [None] * (len(pattern))
    kmp_next[0] = -1
    i = 0
    j = kmp_next[0]
    while i  < len(pattern) - 1:
        while j > -1 and pattern[i] != pattern[j]:
            j = kmp_next[j]
        i += 1
        j += 1
        if pattern[i] == pattern[j]:
            kmp_next[i] = kmp_next[j]
        else:
            kmp_next[i] = j    
    return kmp_next

def process(pattern, kmp, text):
    i,j = 0,0
    while(j < len(text) - 1):
        while i > - 1 and pattern[i] != text[j]:
            i = kmp_next[i]
        i += 1
        j += 1
        if i >= len(pattern) - 1:
            print("Match found at " + str(j - i))
            i = kmp_next[i]


pattern = getopt.getopt(sys.argv[1:],"")[1][0]
file = getopt.getopt(sys.argv[1:],"")[1][1]


with open(file, encoding="utf8", errors='ignore') as f:
    file_text = f.read()
    start = time.time()
    kmp_next = preprocessing(pattern)
    process(pattern, kmp_next, file_text)
    end = time.time()
    print("Elapsed time was: " + str(end - start) + " seconds")
    f.close()