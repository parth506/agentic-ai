from agent import run_agent

def chat():
    print("🧠 Agentic AI - Day 1 Basic Agent")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye 👋")
            break

        response = run_agent(user_input)
        print("\nAgent Response:\n")
        print(response)
        print("\n" + "-"*50 + "\n")


if __name__ == "__main__":
    chat()