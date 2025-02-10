import pandas as pd

# Read the dataset
file_path = 'converted_captions-ne_NP.txt'
df = pd.read_csv(file_path, delimiter=',', header=None)

# Replace empty strings or whitespace-only strings with NaN
df.replace(r'^\s*$', None, regex=True, inplace=True)

# Find rows with empty values in any column
empty_rows = df[df.isna().any(axis=1)]

# Print rows with empty values
print("Rows with empty or missing values:")
print(empty_rows)

# Count empty values in each column
empty_counts = df.isna().sum()
print("\nNumber of empty values in each column:")
print(empty_counts)