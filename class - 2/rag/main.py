from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.os import AgentOS
from indexing import knowledge

agent = Agent(
    name="RAG Agent",
    model=Ollama(id="llama3.2:1b"),
    knowledge=knowledge,
    search_knowledge=True,
    markdown=True,
    description="A Retrieval-Augmented Generation agent that answers questions using indexed knowledge base",
    instructions=[
        "Use the provided knowledge base to answer questions accurately",
        "Search through the knowledge base when answering queries",
        "Provide responses in markdown format for better readability",
        "Be helpful and provide detailed explanations when possible",
    ],
)

agent_os = AgentOS(agents=[agent])
app = agent_os.get_app()

if __name__ == "__main__":
    agent_os.serve(app="main:app", reload=True)