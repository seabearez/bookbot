from stats import get_word_count, get_chars

def main():
    text = get_book_text('books/frankenstein.txt')
    count = get_word_count(text)
    print(f"{count} words found in the document")
    print(f"{get_chars(text)}")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

main()