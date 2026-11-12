"""MCP server with read-only tools against fictional skills data."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("synthetic-skills-inventory")
SKILLS = {"analyst": {"python": 3, "sql": 4}, "designer": {"research": 4, "figma": 3}}

@mcp.tool()
def available_roles() -> list[str]:
    """Return example role identifiers (no real employee data)."""
    return sorted(SKILLS)

@mcp.tool()
def skills_for_role(role: str) -> dict[str, int]:
    """Return example capability ratings for a named role."""
    if role not in SKILLS:
        raise ValueError("Unknown demo role")
    return SKILLS[role]

if __name__ == "__main__":
    mcp.run(transport="stdio")
