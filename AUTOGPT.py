# !pip install bs4
# !pip install nest_asyncio

import os
from dotenv import load_dotenv
import nest_asyncio

# Needed since Jupyter runs an async event loop
nest_asyncio.apply()

load_dotenv()

def get_chatgpt_token():
    chatgpt_token = os.getenv("CHATGPT_TOKEN")
    if chatgpt_token:
        return chatgpt_token
    else:
        raise ValueError("ChatGPT Token is empty. Edit the .env file and add your ChatGPT token.")

def get_huggingchat_credentials():
    email_hf = os.getenv("emailHF")
    psw_hf = os.getenv("pswHF")
    if email_hf and psw_hf:
        return email_hf, psw_hf
    else:
        raise ValueError("HuggingChat credentials are empty. Edit the .env file and add your email and password.")

def initialize_chat_model():
    select_model = input(
        "Select the model you want to use (1, 2, 3, or 4):\n"
        "1) ChatGPT\n"
        "2) HuggingChat\n"
        "3) BingChat\n"
        "4) Google Bard\n"
        ">>> "
    )

    if select_model == "1":
        chatgpt_token = get_chatgpt_token()
        model = "gpt-4" if os.getenv("USE_GPT4") == "True" else "default"
        return ChatGPTAPI.ChatGPT(token=chatgpt_token, model=model)

    elif select_model == "2":
        email_hf, psw_hf = get_huggingchat_credentials()
        # Initialize HuggingChat here
        # ...

    # Add similar logic for other models (BingChat, Google Bard)

if __name__ == "__main__":
    chat_model = initialize_chat_model()
    # Rest of your code goes here
