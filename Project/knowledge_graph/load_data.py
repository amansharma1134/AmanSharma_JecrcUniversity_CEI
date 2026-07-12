from knowledge_graph.kg import KnowledgeGraph

kg = KnowledgeGraph()

kg.create_concept(
    "FAISS",
    "FAISS is an open-source vector similarity search library developed by Facebook AI."
)

kg.create_concept(
    "LangGraph",
    "LangGraph is a framework for building stateful AI agents using LangChain."
)

kg.create_concept(
    "RAG",
    "Retrieval-Augmented Generation combines retrieval with LLM generation."
)

kg.create_concept(
    "Knowledge Graph",
    "A Knowledge Graph stores entities and their relationships."
)

kg.close()

print("Knowledge Graph Loaded Successfully!")