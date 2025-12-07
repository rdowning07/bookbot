from stats import word_count, char_count, sort_chars

def get_books_text(path):
    with open(path, "r") as f:
        content = f.read()
    return content

def main():
    text = get_books_text("books/frankenstein.txt")
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
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