# 🤖 Memory-Augmented Chatbot

A Memory-Augmented AI Chatbot that combines **Hybrid Retrieval-Augmented Generation (RAG)**, **Neo4j Knowledge Graph**, **Long-Term Conversation Memory**, and **LangGraph Workflow** to provide intelligent, context-aware responses using **Ollama (Llama 3.2)**.

---

## 🚀 Features

- 🧠 Long-Term Conversation Memory
- 📚 Hybrid RAG using FAISS Vector Database
- 🕸 Neo4j Knowledge Graph Integration
- 🤖 Ollama (Llama 3.2) for Local LLM Inference
- ⚡ LangGraph Workflow Orchestration
- 🔍 Semantic Search with Sentence Transformers
- 💬 Interactive Streamlit Chat Interface
- 📊 Response Evaluation Metrics
- 📝 Document Chunking & Embedding Pipeline

---

## 🏗 Project Architecture

```
                        User
                          │
                          ▼
                  Streamlit Interface
                          │
                          ▼
                    LangGraph Workflow
                          │
                ┌─────────┴─────────┐
                │                   │
                ▼                   ▼
        Conversation Memory   Query Router
                                    │
                          ┌─────────┴─────────┐
                          ▼                   ▼
                  Knowledge Graph        FAISS Retriever
                          │                   │
                          └─────────┬─────────┘
                                    ▼
                             Ollama Llama 3.2
                                    │
                                    ▼
                              Final Response
```

---

# 📂 Project Structure

```
Memory-Augmented-Chatbot
│
├── app.py
├── requirements.txt
├── .env
│
├── api/
├── app/
├── data/
│   ├── documents/
│   ├── processed/
│   └── embeddings/
│
├── evaluation/
│
├── knowledge_graph/
│
├── langgraph_workflow/
│
├── llm/
│
├── memory/
│
├── rag/
│
├── scraper/
│
├── tools/
│
├── ui/
│
└── vector_db/
```

---

# ⚙ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | User Interface |
| LangGraph | Workflow Orchestration |
| LangChain | AI Framework |
| Ollama | Local LLM Inference |
| Llama 3.2 | Large Language Model |
| FAISS | Vector Database |
| Neo4j | Knowledge Graph |
| Sentence Transformers | Embeddings |
| Pickle | Embedding Storage |

---

# 📦 Installation

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🧠 Install Ollama

Download Ollama

https://ollama.com/download

Pull Llama 3.2

```bash
ollama pull llama3.2
```

Verify

```bash
ollama list
```

---

# 🕸 Setup Neo4j

1. Install Neo4j Desktop
2. Create a Local Database
3. Create a `.env` file

Example

```env
NEO4J_URI=bolt://localhost:xxxx
NEO4J_USER=neo4j
NEO4J_PASSWORD=your_password
```

Load Knowledge Graph

```bash
python -m knowledge_graph.load_data
```

---

# 📚 Create Embeddings

Generate Chunks

```bash
python rag/chunk.py
```

Generate Embeddings

```bash
python rag/embeddings.py
```

Create FAISS Index

```bash
python rag/vector_store.py
```

---

# ▶ Run Chatbot

Terminal Version

```bash
python -m rag.generate
```

Streamlit Version

```bash
streamlit run app.py
```

---

# 💬 Sample Questions

```
What is FAISS?

What is LangGraph?

Explain Retrieval-Augmented Generation.

My name is Aman.

What is my name?

What is a Knowledge Graph?

What is Machine Learning?
```

---

# 📊 Evaluation

The chatbot measures

- Response Time
- Retrieved Chunks
- Knowledge Graph Hits
- Memory Hits
- Answer Token Count

---
## 📸 Screenshots

### 🏠 Streamlit Home Page

![Streamlit Home Page](README_assets/Streamlit%20Home%20Page.jpeg)

---

## 💬 Chat Conversation

![Chat Conversation](README_assets/Chat%20Conversation.jpeg)

---

### 🕸 Neo4j Graph

![Neo4j Graph](README_assets/Neo4j%20Graph.jpeg)

---

## 🧠 Memory Example

![Memory Example](README_assets/Memory%20Example.jpeg)
```

---

# 🔮 Future Improvements

- Multi-document RAG
- PDF Upload Support
- Voice Chat
- User Authentication
- Chat History Export
- Docker Deployment
- Cloud Deployment
- Advanced Evaluation Metrics
- Multi-Agent Workflow
- Hybrid Search (BM25 + FAISS)

---

# 👨‍💻 Author

**Aman Sharma**

B.Tech Computer Science Engineering  
Specialization: Data Science & Data Analytics

GitHub: https://github.com/amansharma1134

LinkedIn: https://linkedin.com/in/amansharma1134

---

# ⭐ If you found this project useful

Please consider giving this repository a ⭐ on GitHub.
