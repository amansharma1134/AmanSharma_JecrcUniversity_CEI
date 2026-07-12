import json
import re

# ============================================================
# Calculator Tool
# ============================================================

def calculator(expression):
    """Safely evaluates a mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return result
    except Exception:
        raise ValueError("Invalid mathematical expression.")


# ============================================================
# Keyword Extraction Tool
# ============================================================

def extract_keywords(text):
    """Extracts important keywords from the given text."""

    stop_words = {
        "the", "is", "a", "an", "and", "or", "to",
        "of", "in", "on", "for", "with", "this",
        "that", "it", "be", "are", "was", "were",
        "as", "at", "by", "from", "into", "about"
    }

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())

    keywords = [
        word for word in words
        if word not in stop_words
    ]

    # Remove duplicates while preserving order
    keywords = list(dict.fromkeys(keywords))

    return keywords


# ============================================================
# General Response Tool
# ============================================================

def general_response(query):
    """Fallback response."""
    return (
        "This query does not match any available tool. "
        "Please use 'calculate' or 'keywords'."
    )


# ============================================================
# Agent Function
# ============================================================

def agent(query):

    print("\n========== VALIDATION ==========")
    print("Original Query :", query)

    query_lower = query.lower().strip()

    print("Lowercase Conversion : Passed")
    print("Routing Decision : Started")

    try:

        # ----------------------------------------------------
        # Calculator Routing
        # ----------------------------------------------------

        if "calculate" in query_lower:

            print("Selected Tool : Calculator")

            expression = query_lower.replace("calculate", "").strip()

            if expression == "":
                return {
                    "type": "error",
                    "result": "No mathematical expression provided."
                }

            result = calculator(expression)

            return {
                "type": "calculation",
                "result": result
            }

        # ----------------------------------------------------
        # Keyword Routing
        # ----------------------------------------------------

        elif "keywords" in query_lower:

            print("Selected Tool : Keyword Extractor")

            text = re.sub(
                r'keywords[: ]*',
                '',
                query,
                flags=re.IGNORECASE
            ).strip()

            if text == "":
                return {
                    "type": "error",
                    "result": "No text provided for keyword extraction."
                }

            result = extract_keywords(text)

            return {
                "type": "keywords",
                "result": result
            }

        # ----------------------------------------------------
        # General Routing
        # ----------------------------------------------------

        else:

            print("Selected Tool : General Response")

            return {
                "type": "general",
                "result": general_response(query)
            }

    except Exception as e:

        return {
            "type": "error",
            "result": str(e)
        }


# ============================================================
# Automated Validation Tests
# ============================================================

test_queries = [
    "calculate 15 + 25",
    "calculate 8 * (5 + 2)",
    "calculate",
    "calculate 10 + *",
    "keywords Artificial Intelligence is transforming education and healthcare.",
    "keywords Machine Learning Deep Learning Neural Networks",
    "keywords",
    "Hello",
    "Who are you?"
]

print("\n")
print("=" * 60)
print(" AUTOMATED VALIDATION TESTS ")
print("=" * 60)

for query in test_queries:

    print("\nQuery:", query)

    response = agent(query)

    print(json.dumps(response, indent=4))


# ============================================================
# Interactive Agent
# ============================================================

print("\n")
print("=" * 60)
print(" AGENT READY ")
print("Type 'exit' to stop.")
print("=" * 60)

while True:

    query = input("\nYou: ")

    if query.lower() == "exit":
        print("Agent terminated.")
        break

    response = agent(query)

    print("\nResponse:")
    print(json.dumps(response, indent=4))