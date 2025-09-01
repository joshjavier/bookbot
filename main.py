import sys
from stats import get_num_words, get_char_count, get_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    char_count = get_char_count(book_text)
    sorted_list = get_sorted_list(char_count)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        char, count = item.values()
        if not char.isalpha():
            continue
        print(f"{char}: {count}")
    print("============= END ===============")

main()
