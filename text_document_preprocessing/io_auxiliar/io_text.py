def read_text(filename, text_parser):
    with open(filename, encoding="utf-8", errors="ignore") as file:
        file_text = file.read()
        text_parser(file_text)

def write_text(filename, body):
    with open(filename, "a",  encoding="utf-8", errors="ignore") as file:
        file.write(body)
        file.close()
