import sys, getopt, time

def preBmBc(pattern):
    num_of_chars = 256
    i = 0
    bmbc = [None] * num_of_chars
    while i < num_of_chars:
        bmbc[i] = len(pattern)
        i += 1
    i = 0
    while i < len(pattern) - 1:
        bmbc[ord(pattern[i])] = len(pattern) - i - 1
        i += 1
    return bmbc

def suffixes(pattern):
    f,g = 0,0
    suffixes = [None] * len(pattern)
    suffixes[len(pattern) - 1] = len(pattern)
    g = len(pattern) - 1
    i = len(pattern) - 2
    while i >= 0:
        if i > g and suffixes[i + len(pattern) - 1 - f ] < i - g:
            suffixes[i] = suffixes[i + len(pattern) - 1 - f ]
        else:
            if i < g:
                g = i
            f = i
            while g >= 0 and pattern[g] == pattern[g + len(pattern) - 1 - f]:
                g -= 1
            suffixes[i] = f - g
        i -= 1
        pass
    return suffixes

def preBmGs(pattern):
    i,j = 0,0
    suff = suffixes(pattern)
    bmgs = [None] * len(pattern)
    while i < len(pattern):
        bmgs[i] = len(pattern)
        i += 1
    i = len(pattern) - 1
    while i >= -1:
        if i == -1 or suff[i] == i + 1:
            while j < len(pattern) - 1 - i:
                if bmgs[j] == len(pattern):
                    bmgs[j] = len(pattern) - 1 - i
                j += 1
        i -= 1
    i = 0
    while i <= len(pattern) - 2:
        bmgs[len(pattern) - 1 - suff[i]] = len(pattern) - 1 - i
        i += 1
    return bmgs

def process(pattern, text, bmbc, bmgs):
    j = 0
    while j <= len(text) - len(pattern):
        i = len(pattern) - 1
        while i >= 0 and pattern[i] == text[i + j]:
            i -= 1
        if i < 0:
            print("Match found at " + str(j))
            j += bmgs[0]
        else:
            try:
                j += max(bmgs[i], bmbc[ord(text[i + j])] - len(pattern) + 1 + i)
            except IndexError:
                break
            
    

pattern = getopt.getopt(sys.argv[1:],"")[1][0]
file = getopt.getopt(sys.argv[1:],"")[1][1]

with open(file, encoding="utf8", errors='ignore') as f:
    file_text = f.read()
    start = time.time()
    bmgs = preBmGs(pattern)
    bmbc = preBmBc(pattern)
    process(pattern, file_text, bmbc, bmgs)
    end = time.time()
    print("Elapsed time was: " + str(end - start) + " seconds")
    f.close()