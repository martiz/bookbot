def count_words(text):
    # Counts the number of words in the given text
    words = text.split()
    return len(words)

def main():
    # Open the file and read its contents
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    # Print the contents of the file
    print(file_contents)

    # Count the number of words and print the result
    word_count = count_words(file_contents)
    print(f"\nThe Frankenstein book contains {word_count} words.")

main()
