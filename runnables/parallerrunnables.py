from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

model = ChatMistralAI(model="mistral-small-2506")

parser = StrOutputParser()

prompt1 = ChatPromptTemplate.from_template(
    "Explain {topic} in short"
)

prompt2 = ChatPromptTemplate.from_template(
    "Explain {topic} in detail"
)

short_chain = RunnableLambda(lambda x: x["short"]) | prompt1 | model | parser

detail_chain = RunnableLambda(lambda x: x["detail"]) | prompt2 | model | parser

chain = RunnableParallel({
    "short": short_chain,
    "detail": detail_chain
})

answer = chain.invoke({
    "short": {"topic": "Data Analysis"},
    "detail": {"topic": "Machine Learning"}
})

print(answer["short"])
print(answer["detail"])