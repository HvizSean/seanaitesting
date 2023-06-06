import langchain
from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

import os

# Retrieve the API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create a Parameter for the OpenAI API Key
llm = ChatOpenAI(openai_api_key=openai_api_key)

chat = ChatOpenAI(temperature=0)

# The following steps are the actual code
response = chat([HumanMessage(content="Can you say write me a happy poem about a dog?")])

print(response)