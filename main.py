from agent import run_agent

while True:
    question = input("Enter a question: ")

    if question.lower() == "exit":
        break   
    result = run_agent(question)
    print("Agent: ", result)