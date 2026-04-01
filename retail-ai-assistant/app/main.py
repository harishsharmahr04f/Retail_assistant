from app.services.chat_service import chat
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    chat()