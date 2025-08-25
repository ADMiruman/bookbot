import sys
from stats import get_word_count
from stats import get_num_charac
from stats import sorted_list

def get_book_text(filepath):
    with open(filepath) as book:
        file_contents = book.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    book_characters = get_num_charac(book_text)
    sorted_chars_count = sorted_list(book_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    for item in sorted_chars_count:
        if item["char"].isalpha() == True:
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()