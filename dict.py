import json
# Dictionary of English to Nepali words
with open("english_nepali_dict_2.json", "r", encoding="utf-8") as file:

    english_nepali_dict = json.load(file)

# Function to replace English words with Nepali words
def replace_words(text, dictionary):
    for english_word, nepali_word in dictionary.items():
        text = text.replace(english_word, nepali_word)
    return text

# Read the Nepali text file
input_file = 'output_text(2)-ne_NP.txt'  # Replace with your file path
with open(input_file, 'r', encoding='utf-8') as file:
    nepali_text = file.read()

# Replace English words in the text
updated_text = replace_words(nepali_text, english_nepali_dict)

# Save the updated text to a new file
output_file = 'updated_nepali_text(2).txt'  # Replace with your desired output file path
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(updated_text)

print(f"Updated text saved to {output_file}")