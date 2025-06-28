from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = str(sys.argv[1])
    text = get_book_text(path)
    num_words = nr_of_words(text)
    num_chars = nr_of_chars(text)
    sorted_dict = sort_dict(num_chars)
    formatted_dict = "\n".join(map(lambda e: str(e[0]) + ": " + str(e[1]), sorted_dict))

    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{formatted_dict}
============= END ===============""")

main()
