from pathlib import Path
from sentence_transformers import SentenceTransformer
import pickle
import os

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Model Loaded Successfully!")

chunk_file = Path("data/processed/chunks.txt")

if not chunk_file.exists():
    raise FileNotFoundError("chunks.txt not found!")

chunks = []

current_chunk = ""

with open(chunk_file, "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("----- Chunk"):
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = ""
        else:
            current_chunk += line

if current_chunk:
    chunks.append(current_chunk.strip())

print(f"Chunks Loaded: {len(chunks)}")

print("Generating embeddings...")

embeddings = model.encode(
    chunks,
    convert_to_numpy=True,
    show_progress_bar=True
)

os.makedirs("data/embeddings", exist_ok=True)

with open("data/embeddings/embeddings.pkl", "wb") as f:
    pickle.dump(
        {
            "chunks": chunks,
            "embeddings": embeddings
        },
        f
    )

print("\nEmbeddings Generated Successfully!")
print("Embedding Shape:", embeddings.shape)
