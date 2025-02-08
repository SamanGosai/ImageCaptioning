from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip
import re

# Load input file
with open("output_text(1) (1).txt", "r", encoding="utf-8") as f:
    text = f.read()

# Function to split text into chunks, ensuring complete sentences
def split_text(text, max_length=5000):
    chunks = []
    
    while len(text) > max_length:
        # Try to split at punctuation marks (., ?, !)
        split_idx = text.rfind('.', 0, max_length)
        if split_idx == -1:
            split_idx = text.rfind('?', 0, max_length)
        if split_idx == -1:
            split_idx = text.rfind('!', 0, max_length)
        if split_idx == -1:
            split_idx = text.rfind('\n', 0, max_length)  # Last resort: split at newline
        
        if split_idx == -1:
            split_idx = max_length  # If no punctuation, just split at max_length

        chunks.append(text[:split_idx+1].strip())  # Include punctuation
        text = text[split_idx+1:].strip()  # Remaining text

    chunks.append(text)  # Add any remaining text
    return chunks

chunks = split_text(text)

# Set up Selenium WebDriver
driver = webdriver.Chrome()

# Open the QuillBot translation page
driver.get("https://quillbot.com/translate")
time.sleep(5)  # Allow time for the page to load

output_text = ""

for chunk in chunks:
    # Wait for the input box to be visible
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//textarea[@id="inputText"]'))
    )
    
    input_box.clear()
    pyperclip.copy(chunk)  # Copy the chunk to clipboard
    input_box.send_keys(Keys.CONTROL, "v")  # Paste from clipboard
    time.sleep(2)  # Allow time for text to appear

    # Click the "Translate" button
    translate_btn = driver.find_element("xpath", '//button[contains(text(), "Translate")]')
    translate_btn.click()
    time.sleep(10)  # Wait for translation to complete

    # Copy the translated text
    output_box = driver.find_element("xpath", '//*[@id="outputText"]')
    output_text += output_box.text + "\n\n"  # Add translated text to output

# Save the translated output to a file
with open("translated_captions.txt", "w", encoding="utf-8") as f:
    f.write(output_text)

print("Translation complete! Check 'translated_captions.txt'.")
driver.quit()
