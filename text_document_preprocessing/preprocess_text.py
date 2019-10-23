import re

def preprocess_text(text):
    result = remove_invalid_characters(text)
    result = result.lower()
    result = remove_stop_words(result)
    return result

def remove_invalid_characters(text):
    return re.sub('[^A-Za-z ]+', '', text)

def remove_stop_words(text):
    stopwords = ['a','an','and','are','as','at','be', 'by', 'for', 'from', 'has', 'he', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'was', 'were', 'will', 'with']
    querywords = text.split()
    resultwords  = [word for word in querywords if word not in stopwords]
    result = ' '.join(resultwords)
    return result

