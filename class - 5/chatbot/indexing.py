from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.lancedb import LanceDb, SearchType

knowledge = Knowledge(
    vector_db=LanceDb(
        table_name="docs",
        uri="tmp/lancedb",
        search_type=SearchType.vector,
        embedder=OllamaEmbedder(id="nomic-embed-text", dimensions=768),
    ),
)

if __name__ == "__main__":
    knowledge.insert(name="MyDoc", path=r".\data\EDGE_Bangladesh_Overview.pdf")