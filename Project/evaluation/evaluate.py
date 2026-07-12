import time


class Evaluation:

    def __init__(self):
        self.start_time = 0
        self.end_time = 0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def response_time(self):
        return round(self.end_time - self.start_time, 3)

    def retrieved_chunks(self, context):

        if not context:
            return 0

        return len(context.split("\n\n"))

    def kg_hit(self, context):

        return bool(context.strip())

    def memory_hit(self, context):

        return bool(context.strip())

    def token_count(self, answer):

        return len(answer.split())

    def report(
        self,
        answer,
        rag_context="",
        kg_context="",
        memory_context=""
    ):

        print("\n")
        print("=" * 55)
        print("Evaluation Report")
        print("=" * 55)

        print("Response Time :", self.response_time(), "sec")
        print("Retrieved Chunks :", self.retrieved_chunks(rag_context))
        print("Knowledge Graph Hit :", self.kg_hit(kg_context))
        print("Memory Hit :", self.memory_hit(memory_context))
        print("Answer Tokens :", self.token_count(answer))

        print("=" * 55)