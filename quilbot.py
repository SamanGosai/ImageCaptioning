import re

def split_text(file_path, chunk_size=4500):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Split text into sentences using regex
    sentences = re.split(r'(?<=[.!?])\s+', text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # If adding the next sentence doesn't exceed the chunk size
        if len(current_chunk) + len(sentence) <= chunk_size:
            current_chunk += sentence + " "
        else:
            # If the current chunk is not empty, save it
            if current_chunk:
                chunks.append(current_chunk.strip())
            # Start a new chunk with the current sentence
            current_chunk = sentence + " "

    # Add the last chunk if it's not empty
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

# Example usage
chunks = split_text('captions.txt')
for i, chunk in enumerate(chunks):
    with open(f'chunk_{i+1}.txt', 'w', encoding='utf-8') as chunk_file:
        chunk_file.write(chunk)