from langchain.chat_models import ChatOpenAI, ChatAnthrolpic
import os

AI = "chatgpt"
if AI == "chatgpt":
    llm = ChatOpenAI(
        model='gpt_4',
        openai_api_key=os.getenv(OPENAI_API_KEY)
    )