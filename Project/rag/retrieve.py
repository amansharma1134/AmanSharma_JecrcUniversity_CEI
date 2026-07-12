import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

print("Loading FAISS index...")

index = faiss.read_index("vector_db/faiss_index.bin")

with open("vector_db/chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def retrieve_context(query, top_k=3):
    """
    Retrieve the most relevant chunks from the FAISS vector database.
    """

    query_embedding = embedding_model.encode([query])

    distances, indices = index.search(
        np.array(query_embedding).astype("float32"),
        top_k
    )

    retrieved_chunks = []

    for idx in indices[0]:
        if idx < len(chunks):
            retrieved_chunks.append(chunks[idx])

    return "\n\n".join(retrieved_chunks)
