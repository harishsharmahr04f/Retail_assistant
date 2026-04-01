from app.agent import RetailAgent

agent = RetailAgent()

def chat():
    print("💬 Chat started (type 'exit')")
    while True:
        user = input("You: ")

        if user.strip().lower() == "exit":
            break

        response = agent.handle(user)
        print("Bot:", response)