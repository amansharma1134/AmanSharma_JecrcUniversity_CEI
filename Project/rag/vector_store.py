import pickle
import numpy as np
import faiss
import os

print("Loading embeddings...")

with open("data/embeddings/embeddings.pkl", "rb") as f:
    data = pickle.load(f)

chunks = data["chunks"]
embeddings = data["embeddings"]

print(f"Chunks Loaded : {len(chunks)}")
print(f"Embedding Shape : {embeddings.shape}")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(np.array(embeddings).astype("float32"))

os.makedirs("vector_db", exist_ok=True)

faiss.write_index(index, "vector_db/faiss_index.bin")

with open("vector_db/chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print("\nFAISS Vector Database Created Successfully!")
print(f"Total vectors stored: {index.ntotal}")
