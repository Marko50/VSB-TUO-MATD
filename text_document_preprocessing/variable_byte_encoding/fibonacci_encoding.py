def fibonacci_variable_byte_encoding(inverted_index):
    compressed = dict()
    for term in inverted_index:
        compressed[term] = fibonacci_encoding_list(inverted_index[term])
    return compressed

def fibonacci_encoding_list(posting_list):
    first_docID = posting_list[0]
    encoded = fibonacci_encoding(first_docID)
    for i in range(0, len(posting_list) - 1):
        gap = posting_list[i + 1] - posting_list[i]
        encoded += fibonacci_encoding(gap)
    return encoded

def largest_fib_less_equal(n,fib):
    fib[0] = 1
    fib[1] = 2
    i = 2
    while fib[i - 1] <= n: 
        fib[i] = fib[i - 1] + fib[i - 2] 
        i += 1
    return (i - 2) 

def fibonacci_encoding(n):
    if n == 1:
        return '11'
    elif n == 2:
        return '011'
    elif n == 3:
        return '0011'
    fib = [0 for i in range(n)] 
    index = largest_fib_less_equal(n, fib) 
    codeword = ['a' for i in range(index + 2)] 
    i = index 
    while (n): 
        codeword[i] = '1'
        n = n - fib[i] 
        i = i - 1
        while (i >= 0 and fib[i] > n): 
            codeword[i] = '0'
            i = i - 1
    codeword[index + 1] = '1'
    return "".join(codeword) 