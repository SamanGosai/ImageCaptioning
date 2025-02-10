import re

def detect_english_words(text):
    """
    Detects English words in a given text using regular expressions.
    """
    # Regular expression to match English words (letters a-z, case insensitive)
    english_word_pattern = re.compile(r'[\u0966-\u096F]+')

    
    # Find all English words in the text
    english_words = english_word_pattern.findall(text)
    
    return english_words

def main():
    # Example Nepali dataset with some English words
    with open("cleaned_captions-ne_NP.txt", "r", encoding="utf-8") as file:
        nepali_dataset = file.read()

    # Detect English words in the dataset
    english_words = detect_english_words(nepali_dataset)

    # Print the detected English words
    if english_words:
        print("Detected English words:")
        for word in english_words:
            print(word)
    else:
        print("No English words detected.")

if __name__ == "__main__":
    main()