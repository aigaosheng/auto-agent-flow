from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_experimental.llms.ollama_functions import OllamaFunctions

load_dotenv()

# async def main():
#     agent = Agent(
#         task="Compare the price of gpt-4o and DeepSeek-V3",
#         # llm=ChatOpenAI(model="gpt-4o"),
#         llm=ChatOllama(model="llama3.2"),
#         # llm=OllamaFunctions(model="llama3.2", format="json"),
#         planner_llm = ChatOllama(model="llama3.2"),
#         use_vision=True,
#     )
#     await agent.run()

# asyncio.run(main())


import asyncio
from browser_use import Agent
from browser_use.agent.views import AgentHistoryList
from langchain_ollama import ChatOllama


async def run_search() -> AgentHistoryList:
    agent = Agent(
        task="Search for latest TSLA price",
        llm=ChatOllama(
            model="qwen2.5:32b-instruct-q4_K_M",
            num_ctx=32000,
        ),
    )

    result = await agent.run()
    return result


async def main():
    result = await run_search()
    print("\n\n", result)


if __name__ == "__main__":
    asyncio.run(main())
