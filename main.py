import sys
from stats import word_count, char_count, sort_chars

def get_books_text(path):
    with open(path, "r") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_books_text(book_path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    num_words = word_count(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    
    chars = char_count(text)
    sorted_chars = sort_chars(chars)

    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()
