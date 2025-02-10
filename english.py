import re

def load_english_word_list():
    # Load a basic set of English words from a file or predefined list
    with open("english_words.txt", "r", encoding="utf-8") as f:
        return set(word.strip().lower() for word in f.readlines())

def find_english_words(text, english_words):
    # Regular expression to extract words (assuming words are space-separated)
    potential_words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    # Filter words that exist in the English dictionary
    english_words_found = [word for word in potential_words if word.lower() in english_words]
    
    return english_words_found

# Load English words from file
english_words = load_english_word_list()

# Read dataset from file
file_path = "updated_nepali_text(2).txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        dataset = file.readlines()

    for sentence in dataset:
        print(find_english_words(sentence.strip(), english_words))

except FileNotFoundError:
    print(f"File '{file_path}' not found.")
