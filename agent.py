from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(
    model="tinyllama",
    temperature=0.3
)

SYSTEM_PROMPT = """

You are a clear and concise reasoning assistant.

Always respond in this exact format:

Reasoning:
- Step-by-step explanation in simple language.

Final Answer:
- Clear final answer in 2-3 sentences.

"""

def run_agent(user_input: str):
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    return response.content