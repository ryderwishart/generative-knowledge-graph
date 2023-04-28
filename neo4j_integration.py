from neo4j import GraphDatabase


class Neo4jHandler:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_triplet(self, source, relation, target):
        with self.driver.session() as session:
            query = (
                "MERGE (s:Node {text: $source}) "
                "MERGE (t:Node {text: $target}) "
                "MERGE (s)-[r:RELATION {type: $relation}]->(t)"
            )
            session.run(query, source=source, relation=relation, target=target)


neo4j_handler = Neo4jHandler("bolt://localhost:7687", "neo4j", "your_password")

triplet = ("cat", "chases", "dog")
neo4j_handler.create_triplet(*triplet)
neo4j_handler.close()
