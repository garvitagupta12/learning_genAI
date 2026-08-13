from click import prompt
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "explain {topic} in simple terms"
)

model = ChatMistralAI(model="mistral-small-2506")

parser = StrOutputParser()

chain = prompt | model | parser 

result = chain.invoke("Data Analysis")
print(result)