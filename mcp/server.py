from mcp.server.fastmcp import FastMCP

mcp = FastMCP("devops-mcp")

import tools

if __name__ == "__main__":
    print("Starting Kubernetes MCP Server...")

    mcp.run(
        transport="streamable-http",
        host="0.0.0.0",
        port=8000
    )