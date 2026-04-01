from app.agent import RetailAgent

agent = RetailAgent()

def whatsapp_simulator(message):
    print(f"📱 WhatsApp Message: {message}")
    response = agent.handle(message)
    print(f"📩 Reply: {response}")