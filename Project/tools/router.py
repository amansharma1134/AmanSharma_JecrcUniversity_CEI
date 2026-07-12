import re

def route_query(query: str):
    """
    Route user queries to either Memory or Knowledge.
    """

    query = query.lower()

    words = re.findall(r"\b[a-zA-Z]+\b", query)

    memory_keywords = {
        "my",
        "me",
        "mine",
        "myself",
        "remember",
        "name"
    }

    # Explicit memory questions
    if "what is my name" in query:
        return "memory"

    if "who am i" in query:
        return "memory"

    if "do you remember" in query:
        return "memory"

    # Any personal keyword
    if any(word in memory_keywords for word in words):
        return "memory"

    # Everything else
    return "knowledge"
