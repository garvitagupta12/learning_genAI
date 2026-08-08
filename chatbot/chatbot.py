from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

print("Enter 1 for funny mode, 2 for sad mode, 3 for angry mode and 4 for happy mode")

type=int(input("enter your mode:"))

if type==1:
    mode="you are a funny ai assistant."
elif type==2:
    mode="you are a sad ai assistant."
elif type==3:
    mode="you are an angry ai assistant."
elif type==4:
    mode="you are a happy ai assistant."

messages = [
    SystemMessage(content=mode)
]

print("------------- WELCOME TO CHATBOT (type 0 to exit) --------------")

while(True):
    prompt=input("You : ")
    if prompt=='0':
        break
    messages.append(HumanMessage(content=prompt))
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    print("Bot : ",response.content)

   
