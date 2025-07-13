import sys
from stats import count_words, count_characters_sorted

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    with open(filepath) as f:
        return f.read()

def analyze_book(book):
    print(f"============ BOOKBOT ============")
    book_content = get_book_text(book)

    print(f"----------- Word Count ----------")
    num_words = count_words(book_content)
    print(f"Found {num_words} total words")
    
    print(f"--------- Character Count -------")
    list_dict = count_characters_sorted(book_content)
    for char_dict in list_dict:
        if char_dict["char"].isalpha():
            print(f"{char_dict["char"]}: {char_dict["num"]}")    

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print(sys.argv[1])
        analyze_book(sys.argv[1])

main()