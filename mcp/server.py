from mcp.server.fastmcp import FastMCP

# Create an MCP Server
mcp = FastMCP("devops-mcp")

import tools

if __name__ == "__main__":
    print("Starting Kubernetes MCP Server...")

    mcp.run()