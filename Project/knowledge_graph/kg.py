from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
import re

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

URI = os.getenv("NEO4J_URI")
USER = os.getenv("NEO4J_USER")
PASSWORD = os.getenv("NEO4J_PASSWORD")


class KnowledgeGraph:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            URI,
            auth=(USER, PASSWORD)
        )

    def close(self):
        self.driver.close()

    def create_concept(self, name, description):

        query = """
        MERGE (c:Concept {name:$name})
        SET c.description=$description
        """

        with self.driver.session() as session:
            session.run(
                query,
                name=name,
                description=description
            )

    def search(self, question):
        """
        Search Knowledge Graph using keywords from the user's question.
        """

        words = re.findall(r"[A-Za-z]+", question)

        with self.driver.session() as session:

            for word in words:

                result = session.run(
                    """
                    MATCH (c:Concept)
                    WHERE toLower(c.name)=toLower($word)
                    RETURN c.description AS description
                    LIMIT 1
                    """,
                    word=word
                )

                record = result.single()

                if record:
                    return record["description"]

        return ""