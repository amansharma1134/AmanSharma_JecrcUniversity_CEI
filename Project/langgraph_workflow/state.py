from typing import TypedDict


class ChatState(TypedDict):

    question: str

    memory: str

    knowledge_graph: str

    rag: str

    answer: str
