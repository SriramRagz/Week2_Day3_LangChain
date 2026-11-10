
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

llm = ChatOpenAI(model="gpt-4o-mini")

prompts = [
    "Explain LangChain in two sentences.",
    "What is the purpose of LangSmith in AI application development?",
    "Explain how tracing helps developers debug an LLM application."
]

for number, prompt in enumerate(prompts, start=1):
    print(f"\n--- Prompt {number} ---")
    print(prompt)

    response = llm.invoke([HumanMessage(content=prompt)])

    print("\nResponse:")
    print(response.content)
