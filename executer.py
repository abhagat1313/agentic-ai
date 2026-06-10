from registry import TOOLS

def execute(tool_name):
    if tool_name is None:
        return "not found"
    
    tool = TOOLS[tool_name]["function"];
    return tool();