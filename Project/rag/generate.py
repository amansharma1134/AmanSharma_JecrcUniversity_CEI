from langgraph_workflow.workflow import graph

print("=" * 60)
print("Memory-Augmented Chatbot with Hybrid RAG")
print("=" * 60)

while True:

    question = input("\nAsk a question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    result = graph.invoke({
        "question": question,
        "memory": "",
        "knowledge_graph": "",
        "rag": "",
        "answer": ""
    })

    print("\nBot:\n")
    print(result["answer"])
