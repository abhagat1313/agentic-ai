from planner import plan
from executer import execute

def run_agent(question):
    tool_name = plan(question)
    results = []
    for tool in tool_name:
        results.append(execute(tool))
    return " & ".join(results)