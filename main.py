from stats import word_count, char_count

def get_books_text(path):
    with open(path, "r") as f:
        content = f.read()
    return content

def main():
    text = get_books_text("books/frankenstein.txt")
    num_words = word_count(text)
    print(f"Found {num_words} total words")
    chars = char_count(text)
    print(chars)


main()