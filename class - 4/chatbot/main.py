from agno.agent import Agent
from agno.models.ollama import Ollama
from indexing import knowledge


def get_agent() -> Agent:
    return Agent(
        name="EDGE Chatbot",
        model=Ollama(id="llama3.2:1b"),
        # Disable automatic tool-based search — llama3.2:1b struggles with tool schemas
        search_knowledge=False,
        markdown=True,
        description = ["A helpful assistant for EDGE Bangladesh that answers questions clearly and politely using only the information provided."],
        instructions = [
            "You are a helpful and professional assistant for EDGE Bangladesh.",
            "Provide accurate and concise answers based only on the given context.",
            "Do not use outside knowledge or make assumptions beyond the provided context.",
            "If the answer is not available in the context, respond with: 'I don't know based on the provided information.'",
            "Maintain a polite and friendly tone; greetings such as 'hello', 'hi', and 'goodbye' are allowed when appropriate.",
        ]
    )


def ask(query: str) -> str:
    """Manually retrieve context then query the agent."""
    # 1. Search the knowledge base ourselves
    results = knowledge.search(query, max_results=3)
    if results:
        context = "\n\n".join(r.content for r in results if r.content)
    else:
        context = "No relevant documents found."

    # 2. Build a grounded prompt
    prompt = f"""Context from knowledge base:
{context}

Question: {query}"""

    agent = get_agent()
    response = agent.run(prompt)
    return response.content if hasattr(response, "content") else str(response)