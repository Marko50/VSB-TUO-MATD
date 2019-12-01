from math import log

def tf_idf_weights(inverted_index, term_frequency):
    inv_doc_freq = inverse_document_frequency(inverted_index, len(term_frequency))
    tf_idf = dict()
    for term, posting_list in inverted_index.items():
        for post in posting_list:
            tf_idf[(term,post)] = inv_doc_freq[term] * term_frequency[post][term] 
    return tf_idf

def inverse_document_frequency(inverted_index, N):
    inv_doc_freq = dict()
    for term, posting_list in inverted_index.items():
        inv_doc_freq[term] = log(N/len(posting_list))
    return inv_doc_freq

    