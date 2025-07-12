from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import asyncio

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")


async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["/Users/mern/Dev/mcp/mcp-crash-course/servers/math_server.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://localhost:8000/sse",
                "transport": "sse",
            },
        }
    )

    tools = await client.get_tools()
    agent = create_react_agent(llm, tools)
    # result = await agent.ainvoke({"messages": "What is 2 + 2?"})
    result = await agent.ainvoke({"messages": "What is the weather in alaska?"})
    print(result["messages"][-1].content)

    # print("Hello from langchain_client.py")


if __name__ == "__main__":
    asyncio.run(main())
