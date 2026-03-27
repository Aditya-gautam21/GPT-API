import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
#from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

query = input("\nWhat can i help you with?\n")
AI = "chatgpt"

if AI == "chatgpt":
    llm = ChatOpenAI(
        model='gpt-4o-mini',
        openai_api_key=os.getenv("OPENAI_API_KEY")
    )

    response = llm.invoke(query)

elif AI == "claude":
    llm = ChatAnthropic(
        model='claude-3-sonnet-20240229',
        anthropic_api_key=os.getenv('CLAUDE_API_KEY')
    )

    response = llm.invoke('hello')

print(response.content)