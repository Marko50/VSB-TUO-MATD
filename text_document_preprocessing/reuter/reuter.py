from io_auxiliar.io_text import write_text
from text_preprocessement.preprocess_text import preprocess_text

def preprocess_reuter(text):
    TITLE_BEGIN = "<TITLE>"
    TITLE_END = "</TITLE>"
    BODY_BEGIN = "<BODY>"
    BODY_END = "</BODY>"

    # import pudb; pudb.set_trace()
    while True:
        begin_title = text.find(TITLE_BEGIN)
        if begin_title == -1:
            break
        end_title = text.find(TITLE_END)
        begin_body = text.find(BODY_BEGIN)
        end_body = text.find(BODY_END)
        title = extract_text(text, begin_title + len(TITLE_BEGIN), end_title)
        body = extract_text(text, begin_body + len(BODY_BEGIN), end_body)
        output_text(title, body)
        text = text[(end_body + len(BODY_END)):len(text)]

def extract_text(text, begin, end):
    return text[begin:end]

def output_text(title, body):
    title = preprocess_text(title)
    body = preprocess_text(body)
    write_text("output/" + title + ".txt", body)