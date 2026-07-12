from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
import os

documents_path = Path("data/documents")

text = ""

# Read all text files from data/documents
for file in documents_path.glob("*.txt"):
    print(f"Reading: {file}")
    with open(file, "r", encoding="utf-8") as f:
        text += f.read() + "\n"

print(f"\nTotal characters read: {len(text)}")

if not text.strip():
    raise ValueError("No text found inside data/documents")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.split_text(text)

os.makedirs("data/processed", exist_ok=True)

with open("data/processed/chunks.txt", "w", encoding="utf-8") as f:
    for i, chunk in enumerate(chunks):
        f.write(f"----- Chunk {i+1} -----\n")
        f.write(chunk)
        f.write("\n\n")

print(f"\nTotal Chunks Created: {len(chunks)}")
print("Chunks saved successfully!")
