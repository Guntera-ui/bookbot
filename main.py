from stats import word_count, count_chars, sorted_list_dict
import sys


def get_book_text(file_path):
    with open(file_path) as file:
        text = file.read()
        return text


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        text = get_book_text(file_path)
        print("========== BOOKBOT ==========")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        num_words = word_count(text)
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        sorted_char = sorted_list_dict(count_chars(text))
        for item in sorted_char:
            print(f"{item['char']}: {item['num']}")
        print("========== END ==========")


main()
