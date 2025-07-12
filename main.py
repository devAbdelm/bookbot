from stats import count_words
from stats import count_chars
from stats import sorted_dictionaries
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_to_file = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    book_text = get_book_text(path_to_file)
    words = count_words(book_text)
    chars = count_chars(book_text)
    organized_chars = sorted_dictionaries(chars)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at",path_to_file+"...")
    print("----------- Word Count ----------")
    print("Found",words,"total words")
    print("--------- Character Count -------")
    for dict in organized_chars:
        char = dict.get("char")

        if char.isalpha():
            print(char+":",dict.get("num"))

    print("============= END ===============")

main()