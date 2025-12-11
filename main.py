import sys
from stats import count_words
from stats import number_of_characters
from stats import sort_on
from stats import convert
from stats import print_sorted
#from stats import sort 


def get_book_text(filepath):
    with open(filepath) as f:
        content = f.read()
    return content


def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = count_words(text)
    char_count = number_of_characters(text)
    report0= convert(char_count)
    report0.sort(reverse=True, key=sort_on)


    print(f"Found {num_words} total words")
    print(f"Character counts: {char_count}")
    print_sorted(report0)

main()


