import sys

from stats import count_chars, count_words


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def pretty_print_word_report(word_count):
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")


def pretty_print_char_report(char_list):
    print("--------- Character Count -------")
    for char in char_list:
        print(f"{char["char"]}: {char["num"]}")


def pretty_print_book_report(book, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")

    pretty_print_word_report(word_count)
    pretty_print_char_report(char_list)

    print("============= END ===============")


def get_book_path():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]


def main():
    book = get_book_path()
    book_text = get_book_text(book)

    word_count = count_words(book_text)
    chars_list = count_chars(book_text)

    pretty_print_book_report(book, word_count, chars_list)


main()
