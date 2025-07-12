# MCP  - Langchain 

A learning project demonstrating the **Model Context Protocol (MCP)** with multiple server implementations and a LangChain client integration.

## Overview

This application showcases how to build and integrate MCP servers with AI agents using LangChain and LangGraph. It includes two different types of MCP servers and a client that can interact with both simultaneously.

## Project Structure

```
mcp-crash-course/
├── servers/
│   ├── math_server.py      # MCP server for mathematical operations
│   └── weather_server.py   # MCP server for weather data
├── langchain_client.py     # LangChain client with agent integration
├── main.py                 # Basic MCP client example
└── pyproject.toml          # Project dependencies
```

## Features

### 🧮 Math Server
- **Transport**: stdio (command-line process)
- **Capabilities**: Basic arithmetic operations, advanced calculations
- **Usage**: Handles mathematical queries and computations

### 🌤️ Weather Server  
- **Transport**: SSE (Server-Sent Events over HTTP)
- **Capabilities**: Weather forecasts, alerts, location-based data
- **Usage**: Provides real-time weather information

### 🤖 LangChain Integration
- **Multi-server client**: Connects to both servers simultaneously
- **Agent integration**: Uses LangGraph's ReAct agent pattern
- **Tool access**: AI agent can use both math and weather tools seamlessly

## Getting Started

### Prerequisites
- Python 3.12+
- UV package manager

### Installation

1. Install dependencies:
```bash
uv sync
```

2. Run the LangChain client:
```bash
uv run langchain_client.py
```

3. Run the basic MCP client:
```bash
uv run main.py
```

## Usage Examples

The application can handle queries like:
- "What is 2 + 2?" (uses math server)
- "What's the weather in Alaska?" (uses weather server)
- "Calculate 15% tip on $50 and tell me if it's good weather for dining out" (uses both servers)

## Learning Objectives

This crash course demonstrates:
1. **MCP Server Development**: How to create servers with different transports
2. **Multi-server Architecture**: Managing multiple MCP servers in one application
3. **LangChain Integration**: Using MCP servers as tools in AI agents
4. **Transport Protocols**: stdio vs SSE transport methods
5. **Agent Patterns**: ReAct agent pattern with tool selection

## Key Technologies

- **MCP (Model Context Protocol)**: Protocol for AI-server communication
- **LangChain**: Framework for building AI applications
- **LangGraph**: Library for creating agent workflows
- **OpenAI GPT**: Language model for agent reasoning
- **asyncio**: Asynchronous programming for server communication

## Configuration

The `langchain_client.py` configures servers with specific transport methods:

```python
{
    "math": {
        "command": "python",
        "args": ["servers/math_server.py"],
        "transport": "stdio"
    },
    "weather": {
        "url": "http://localhost:8000/sse", 
        "transport": "sse"
    }
}
```

## Next Steps

- Extend servers with more capabilities
- Add authentication and security
- Implement WebSocket transport
- Create custom tool integrations
- Build multi-modal server interactions
