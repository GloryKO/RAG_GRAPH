# app.py
import streamlit as st
import os 
from dotenv import load_dotenv
from knowledge_graph import KnowledgeGraph
from llm_graph_transformer import LLMGraphTransformer
load_dotenv()

def main():
    # Initialize the knowledge graph with real data
    kg_data = [
        {"name": "Inception", "type": "Movie", "relations": [
            {"name": "Christopher Nolan", "type": "Director", "relationship": "directed"},
            {"name": "Leonardo DiCaprio", "type": "Actor", "relationship": "starred"},
            {"name": "Science Fiction", "type": "Genre", "relationship": "is_genre"}
        ]},
        {"name": "The Matrix", "type": "Movie", "relations": [
            {"name": "Lana Wachowski", "type": "Director", "relationship": "directed"},
            {"name": "Keanu Reeves", "type": "Actor", "relationship": "starred"},
            {"name": "Science Fiction", "type": "Genre", "relationship": "is_genre"}
        ]},
        {"name": "Interstellar", "type": "Movie", "relations": [
            {"name": "Christopher Nolan", "type": "Director", "relationship": "directed"},
            {"name": "Matthew McConaughey", "type": "Actor", "relationship": "starred"},
            {"name": "Science Fiction", "type": "Genre", "relationship": "is_genre"}
        ]},
        {"name": "Mad Matt", "type": "Movie", "relations": [
            {"name": "George Kolade", "type": "Director", "relationship": "directed"},
            {"name": "Tom Hardy", "type": "Actor", "relationship": "starred"},
            {"name": "Action", "type": "Genre", "relationship": "is_genre"}
        ]}
    ]

    kg_data.append({
            "name": "New One", "type": "Movie", "relations": [
                {"name": "Glory Kolade", "type": "Director", "relationship": "directed"},
                {"name": "Boluwatife Rolland", "type": "Actor", "relationship": "starred"},
                {"name": "Drama", "type": "Genre", "relationship": "is_genre"}
            ]
        })
    
    graph = KnowledgeGraph()
    graph.add_data(kg_data)
    # context = graph.retrieve_context("who directed the movie 'new one'")
    #print(context)

    # Get OpenAI API key from environment
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        st.error("OpenAI API key not found. Please set it in the .env file.")
        return

    transformer = LLMGraphTransformer(graph, openai_api_key=openai_api_key)

    # Streamlit UI
    st.title("RAG with LangChain and Knowledge Graph")

    query = st.text_input("Enter your query:")

    if st.button("Submit"):
        if query.strip():
            response = transformer.generate_response(query)
            st.write(f"Response: {response}")
        else:
            st.error("Query cannot be empty. Please enter a valid query.")

if __name__ == "__main__":
    main()