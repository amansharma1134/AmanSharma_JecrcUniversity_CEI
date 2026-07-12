import streamlit as st
import time

from langgraph_workflow.workflow import graph
from memory.memory import ChatMemory

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Memory-Augmented Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 Memory-Augmented Chatbot")

st.markdown("""
### Hybrid RAG + Knowledge Graph + Long-Term Memory

This chatbot uses:

- 🧠  Long-Term Memory
- 📚  FAISS Vector Database
- 🕸  Neo4j Knowledge Graph
- 🤖  Ollama (Llama 3.2)
- ⚡   LangGraph Workflow
""")

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("🚀 Project Features")

    st.success("✔ LangGraph")

    st.success("✔ Ollama")

    st.success("✔ FAISS")

    st.success("✔ Neo4j")

    st.success("✔ Long-Term Memory")

    st.success("✔ Streamlit")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# --------------------------------------------------
# Chat Memory
# --------------------------------------------------

memory = ChatMemory()

with st.expander("🧠 Conversation Memory"):

    st.text(memory.get_context())

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:

    st.session_state.messages = []

# --------------------------------------------------
# Display Previous Messages
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# --------------------------------------------------
# Chat Input
# --------------------------------------------------

prompt = st.chat_input("Ask anything...")

retrieved_context = ""

kg_context = ""

if prompt:

    st.session_state.messages.append(

        {

            "role": "user",

            "content": prompt

        }

    )

    with st.chat_message("user"):

        st.markdown(prompt)

    start = time.time()

    with st.spinner("🤖 Thinking..."):

        result = graph.invoke(

            {

                "question": prompt,

                "memory": "",

                "knowledge_graph": "",

                "rag": "",

                "answer": ""

            }

        )

    end = time.time()

    response_time = round(end - start, 2)

    response = result.get("answer", "No response generated.")

    retrieved_context = result.get("rag", "")

    kg_context = result.get("knowledge_graph", "")

    st.session_state.messages.append(

        {

            "role": "assistant",

            "content": response

        }

    )

    with st.chat_message("assistant"):

        st.markdown(response)

        st.caption(f"⏱ Response Time: {response_time} sec")

# --------------------------------------------------
# Retrieved Context
# --------------------------------------------------

with st.expander("📚 Retrieved Context"):

    if retrieved_context:

        st.write(retrieved_context)

    else:

        st.info("No retrieved context available.")

# --------------------------------------------------
# Knowledge Graph
# --------------------------------------------------

with st.expander("🕸 Knowledge Graph"):

    if kg_context:

        st.write(kg_context)

    else:

        st.info("No Knowledge Graph information available.")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption("Developed using Streamlit • LangGraph • Ollama • Neo4j • FAISS")