import requests

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2",
        "prompt": "Explain Retrieval-Augmented Generation in two sentences.",
        "stream": False
    }
)

print(response.json()["response"])
