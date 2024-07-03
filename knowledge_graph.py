
import networkx as nx
import logging
logging.basicConfig(level=logging.INFO)


class KnowledgeGraph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_data(self, data):
        for item in data:
            self.graph.add_node(item["name"], type=item["type"])
            for relation in item.get("relations", []):
                self.graph.add_node(relation["name"], type=relation["type"])
                self.graph.add_edge(item["name"], relation["name"], relationship=relation["relationship"])
        # logging.info(f"Graph nodes: {self.graph.nodes(data=True)}")
        # logging.info(f"Graph edges: {self.graph.edges(data=True)}")

    def retrieve_context(self, query):
        # Normalize query for case-insensitive matching
        query_lower = query.lower()
        nodes = self.graph.nodes(data=True)
        
        # Match nodes directly mentioned in the query
        relevant_nodes = []
        for node, attr in nodes:
            if node.lower() in query_lower or any(rel.lower() in query_lower for rel in [attr.get('type', '')]):
                relevant_nodes.append(node)
        
        context = []
        for node in relevant_nodes:
            neighbors = list(self.graph.neighbors(node))
            for neighbor in neighbors:
                relationship = self.graph[node][neighbor]['relationship']
                context.append(f"{node} ({relationship}) {neighbor}")

        # logging.info(f"Relevant nodes: {relevant_nodes}")
        # logging.info(f"Context: {context}")

        return " ".join(context)
