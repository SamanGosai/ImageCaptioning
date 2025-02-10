import re

# Function to remove all special characters (including . and ,)
def remove_all_special_characters(text):
    # Define a regex pattern to keep only alphanumeric characters and spaces
    pattern = r"[^a-zA-Z0-9\s]"
    return re.sub(pattern, '', text)

# Read the captions from the original file
with open("captions.txt", "r") as file:
    captions = file.readlines()

# Clean the captions by removing all special characters
cleaned_captions = [remove_all_special_characters(caption) for caption in captions]

# Save the cleaned captions to a new file
with open("cleaned_captions.txt", "w") as file:
    for caption in cleaned_captions:
        file.write(caption.strip() + "\n")  # Ensure each caption is on a new line

print("All special characters removed and cleaned captions saved to cleaned_captions.txt")