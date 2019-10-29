from porter import PorterStemmer
import re


def preprocess_text(text):
    result = remove_invalid_characters(text)
    result = result.lower()
    result = remove_stop_words(result)
    result = porter_stemming(result)
    return result

def porter_stemming(text):
    p = PorterStemmer()
    result = ""
    for word in text.split():
        result += p.stem(word, 0, len(word) - 1) + " "
    return result

def remove_invalid_characters(text):
    return re.sub('[^A-Za-z \n]+', '', text)


def remove_stop_words(text):
    stopwords = ['a','an','and','are','as','at','be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
    querywords = text.split()
    resultwords  = [word for word in querywords if word not in stopwords]
    result = ' '.join(resultwords)
    return result

