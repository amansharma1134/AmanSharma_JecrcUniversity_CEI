from langgraph.graph import StateGraph, END

from langgraph_workflow.state import ChatState
from memory.memory import ChatMemory
from knowledge_graph.kg import KnowledgeGraph
from rag.retrieve import retrieve_context
from rag.llm import generate_llm_response
from tools.router import route_query
from evaluation.evaluate import Evaluation

# --------------------------------------------------
# Initialize Components
# --------------------------------------------------

memory = ChatMemory()
kg = KnowledgeGraph()
evaluator = Evaluation()

# --------------------------------------------------
# Memory Node
# --------------------------------------------------

def memory_node(state: ChatState):

    state["memory"] = memory.get_context()

    return state


# --------------------------------------------------
# Knowledge Graph Node
# --------------------------------------------------

def kg_node(state: ChatState):

    state["knowledge_graph"] = kg.search(state["question"])

    return state


# --------------------------------------------------
# RAG Node
# --------------------------------------------------

def rag_node(state: ChatState):

    state["rag"] = retrieve_context(state["question"])

    return state


# --------------------------------------------------
# LLM Node
# --------------------------------------------------

def llm_node(state: ChatState):

    route = route_query(state["question"])

    print("\n" + "=" * 70)
    print(f"Route Selected : {route}")
    print("=" * 70)

    if route == "memory":

        prompt = f"""
You are a helpful AI assistant.

Use ONLY the conversation memory.

If the answer is unavailable in memory,
say you don't know.

Conversation Memory:

{state["memory"]}

Question:

{state["question"]}

Answer:
"""

    else:

        prompt = f"""
You are a helpful AI assistant.

Answer according to these priorities:

1. Use the Knowledge Graph first.
2. If not found, use Retrieved Documents.
3. If both are empty, answer using your own knowledge.
4. Do NOT use conversation memory for factual questions.

Knowledge Graph:

{state["knowledge_graph"]}

Retrieved Documents:

{state["rag"]}

Question:

{state["question"]}

Answer:
"""

    print("\n" + "=" * 70)
    print("PROMPT SENT TO LLM")
    print("=" * 70)
    print(prompt)
    print("=" * 70)

    evaluator.start()

    answer = generate_llm_response(prompt)

    evaluator.stop()

    evaluator.report(
        answer,
        rag_context=state["rag"],
        kg_context=state["knowledge_graph"],
        memory_context=state["memory"]
    )

    memory.save_memory(
        state["question"],
        answer
    )

    state["answer"] = answer

    return state


# --------------------------------------------------
# Build LangGraph Workflow
# --------------------------------------------------

builder = StateGraph(ChatState)

builder.add_node("Memory", memory_node)
builder.add_node("KnowledgeGraph", kg_node)
builder.add_node("RAG", rag_node)
builder.add_node("LLM", llm_node)

builder.set_entry_point("Memory")

builder.add_edge("Memory", "KnowledgeGraph")
builder.add_edge("KnowledgeGraph", "RAG")
builder.add_edge("RAG", "LLM")
builder.add_edge("LLM", END)

graph = builder.compile()