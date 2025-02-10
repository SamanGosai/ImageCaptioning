import pandas as pd

# Load the CSV file
df = pd.read_csv("results.csv", delimiter="|")

# Strip leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Print column names to confirm
print("Column names after stripping spaces:", df.columns.tolist())

# Replace NaN values with an empty string
captions = df['comment'].fillna("")

# Save captions to a text file
with open("captions.txt", "w") as file:
    for caption in captions:
        file.write(caption.strip() + "\n")

print("Captions saved to captions.txt")