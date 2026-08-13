from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

model = ChatMistralAI(model="mistral-small-2506")
parser = StrOutputParser()

prompt1= ChatPromptTemplate.from_messages([
        ("system" ,"you are a code generator" ),
        ("human","{topic}")
])

prompt2= ChatPromptTemplate.from_messages([
        ("system" , "you explains thing in simple terms which is easy to understand"),
        ("human","explain the following code {code} ")
])

sequence1 = prompt1 | model | parser 

sequence2 = RunnableParallel({
    "code" : RunnablePassthrough(),
    "explanation" : prompt2 | model | parser
})

chain = sequence1 | sequence2

result = chain.invoke({"topic" : "write a code of palindrome in python"})
print(result['code'])
print(result['explanation']) 