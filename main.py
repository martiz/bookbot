import sys

from stats import (
    count_words,
    character_frequencies,
    sorted_count
)

def main():
    # file_path = "books/frankenstein.txt"

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    text = get_book_text(file_path)
    # print(text)

    # Count the number of words and print the result
    word_count = count_words(text)
    # print(f"\n{word_count} words found in the document.")

    # Count character frequencies and print the result
    char_freq = character_frequencies(text)
    # print("\nCharacter frequencies:")
    # print(char_freq)

    # Sorting characters according to the count
    sorted_char_freq = sorted_count(char_freq)

    # Generate the report
    generate_report(file_path, word_count, sorted_char_freq)

def generate_report(file_path, word_count, sorted_char_freq):
    # Generates a formatted report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    # Print character frequencies in descending order
    # for char, freq in sorted_char_freq:
    for item in sorted_char_freq:
        # print(f"The '{char}' character was found {freq} times")
        # print(f"{char}: {freq}")
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

def get_book_text(file_path):
    ## Open the file and read its contents
    with open(file_path) as f:
        return f.read()

main()
