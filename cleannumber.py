import re

def replace_nepali_numbers(text):
    nepali_numbers = {
        "०": "शून्य", "१": "एक", "२": "दुई", "३": "तीन", "४": "चार", "५": "पाँच", "६": "छ", "७": "सात", "८": "आठ", "९": "नौ",
        "१०": "दस", "११": "एघार", "१२": "बाह्र", "१३": "तेह्र", "१४": "चौध", "१५": "पन्ध्र", "१६": "सोह्र", "१७": "सत्र", "१८": "अठार", "१९": "उन्नाइस",
        "२०": "बीस", "२१": "एक्काइस", "२२": "बाइस", "२३": "तेइस", "२४": "चौबीस", "२५": "पच्चीस", "२६": "छब्बीस", "२७": "सत्ताइस", "२८": "अठ्ठाइस", "२९": "उनन्तीस",
        "३०": "तीस", "३१": "एकतीस", "३२": "बत्तीस", "३३": "तेत्तीस", "३४": "चौँतीस", "३५": "पैँतीस", "३६": "छत्तीस", "३७": "सैँतीस", "३८": "अठतीस", "३९": "उनन्चालीस",
        "४०": "चालीस", "४१": "एकचालीस", "४२": "बयालीस", "४३": "त्रियालीस", "४४": "चवालीस", "४५": "पैंतालीस", "४६": "छयालीस", "४७": "सतचालीस", "४८": "अठचालीस", "४९": "उनन्चास",
        "५०": "पचास", "६०": "साठी", "७०": "सत्तरी", "८०": "असी", "९०": "नब्बे",
        "१००": "सय", "१०००": "हजार"
    }

    # Function to convert numbers to Nepali words
    def convert_number(num):
        num_str = str(num)
        if num_str in nepali_numbers:
            return nepali_numbers[num_str]  # Directly return if found in dictionary
        
        elif num < 100:
            tens = (num // 10) * 10  # Extract tens (e.g., 40, 50)
            ones = num % 10  # Extract ones (e.g., 4 in 44)
            
            # Convert tens and ones to Nepali numerals
            tens_nepali = str(tens).translate(str.maketrans("0123456789", "०१२३४५६७८९"))
            ones_nepali = str(ones).translate(str.maketrans("0123456789", "०१२३४५६७८९"))
            
            tens_str = nepali_numbers.get(tens_nepali, '')
            ones_str = nepali_numbers.get(ones_nepali, '')
            
            return (tens_str + " " + ones_str).strip()
        
        elif num < 1000:
            hundreds = num // 100
            remainder = num % 100
            
            hundreds_nepali = str(hundreds).translate(str.maketrans("0123456789", "०१२३४५६७८९"))
            
            if remainder == 0:
                return nepali_numbers[hundreds_nepali] + " सय"
            
            return nepali_numbers[hundreds_nepali] + " सय " + convert_number(remainder)

        else:
            thousands = num // 1000
            remainder = num % 1000
            
            thousands_nepali = str(thousands).translate(str.maketrans("0123456789", "०१२३४५६७८९"))
            
            if remainder == 0:
                return nepali_numbers[thousands_nepali] + " हजार"
            
            return nepali_numbers[thousands_nepali] + " हजार " + convert_number(remainder)

    def replace_match(match):
        nepali_num = match.group()
        arabic_num = int(nepali_num.translate(str.maketrans("०१२३४५६७८९", "0123456789")))  # Convert Nepali to Arabic
        
        return convert_number(arabic_num)
    
    return re.sub(r"[०१२३४५६७८९]+", replace_match, text)

def process_file(filename, output_filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()
    
    converted_content = [replace_nepali_numbers(line) for line in content]
    
    with open(output_filename, "w", encoding="utf-8") as file:
        file.writelines(converted_content)

# Process the given file and save the output to a new file
process_file("updated_nepali_text(2).txt", "converted_captions-ne_NP.txt")
