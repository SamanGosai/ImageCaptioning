import re

def detect_english_words(text):
    """
    Detects English words in a given text using regular expressions.
    Allows words with hyphens and apostrophes.
    """
    # Improved regex for English words (allows hyphens and apostrophes)
    english_word_pattern = re.compile(r"\b[a-zA-Z][a-zA-Z'-]*[a-zA-Z]?\b")

    # Find all English words in the text
    english_words = english_word_pattern.findall(text)

    return english_words

def process_file(file_path):
    """
    Reads the dataset from a file and detects English words.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        # Detect English words
        english_words = detect_english_words(text)

        # Print the detected English words
        if english_words:
            print("Detected English words:")
            for word in english_words:
                print(word)
        else:
            print("No English words detected.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = "updated_nepali_text(2).txt"  # Change if the filename is different
    process_file(file_path)
