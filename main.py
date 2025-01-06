def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    # Count the number of words and print the result
    word_count = count_words(text)
    # print(f"\n{word_count} words found in the document.")
    # Count character frequencies and print the result
    char_freq = character_frequencies(text)
    # print("\nCharacter frequencies:")
    # print(char_freq)
    # Generate the report
    generate_report(file_path, word_count, char_freq)

def generate_report(file_path, word_count, char_freq):
    # Generates a formatted report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    # Convert the dictionary to a list of tuples and sort by frequency
    sorted_char_freq = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)

    # Print character frequencies in descending order
    for char, freq in sorted_char_freq:
        print(f"The '{char}' character was found {freq} times")

    print("--- End report ---")

def character_frequencies(text):
    # Counts the frequency of each character in the text
    text = text.lower()     # Convert the text to lowercase
    frequency = {}          # Initialize an empty dictionary
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

def count_words(text):
    # Counts the number of words in the given text
    words = text.split()
    return len(words)

def get_text(file_path):
    ## Open the file and read its contents
    with open(file_path) as f:
        return f.read()

main()
