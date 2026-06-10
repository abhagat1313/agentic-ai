def plan(question):
    q = question.lower();
    tools = []
    if "weather" in q:
        tools.append("weather")
    if "time" in q:
        tools.append("time")
    if "stock" in q:
        tools.append("stock")
    return tools