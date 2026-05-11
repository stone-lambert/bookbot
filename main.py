from stats import print_report
import sys


def main():
    # book_text = get_book_text("books/frankenstein.txt")
    # #print("Found", get_num_words(book_text), "total words")
    # #print(get_characters(book_text))
    if len(sys.argv) > 1:
        print_report(sys.argv[1])
    else:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)


main()