from stats import get_book_words, get_book_chars, sort_book_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    get_book_words(book)
    character_dict = get_book_chars(book)
    sort_book_chars(character_dict)
main()
