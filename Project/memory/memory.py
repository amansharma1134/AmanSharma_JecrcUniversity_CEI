import json
import os


class ChatMemory:
    def __init__(self, memory_file="memory/chat_memory.json"):
        self.memory_file = memory_file

        os.makedirs(os.path.dirname(memory_file), exist_ok=True)

        if not os.path.exists(memory_file):
            with open(memory_file, "w", encoding="utf-8") as f:
                json.dump([], f)

    def load_memory(self):
        with open(self.memory_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save_memory(self, user_query, bot_response):
        memory = self.load_memory()

        memory.append({
            "user": user_query,
            "assistant": bot_response
        })

        # Keep only last 10 conversations
        memory = memory[-10:]

        with open(self.memory_file, "w", encoding="utf-8") as f:
            json.dump(memory, f, indent=4)

    def get_context(self):
        memory = self.load_memory()

        context = ""

        for chat in memory:
            context += f"User: {chat['user']}\n"
            context += f"Assistant: {chat['assistant']}\n"

        return context
