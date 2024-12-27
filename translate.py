input_file = "captions.csv"
output_file = "captions(2).csv"
special_char = "|"
with open(input_file, 'r', encoding="utf-8") as infile, open(output_file, 'w',encoding="utf-8") as outfile:
    for line in infile:
        result = line.split(special_char, 1)[1]

        outfile.write(result)

print("new file created!")

