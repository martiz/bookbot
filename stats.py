def count_words(text):
    # Counts the number of words in the given text
    words = text.split()
    return len(words)

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

# Sorting dictionary entries
def sort_on(dict):
    return dict["num"]

def sorted_count(char_freq):
    sorted_list = []
    for char in char_freq:
        sorted_list.append({"char": char, "num": char_freq[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
