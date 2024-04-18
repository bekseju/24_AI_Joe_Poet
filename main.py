from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI()
# result = llm.invoke("how can langsmith help with testing?")
# print(result)

from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])
# chain = prompt | llm 
# result = chain.invoke({"input": "how can langsmith help with testing?"})
# print(result)

from langchain_core.output_parsers import StrOutputParser
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
result = chain.invoke({"input": "how can langsmith help with testing?"})
print(result)


# from langchain_core.prompts import ChatPromptTemplate
# prompt = ChatPromptTemplate.from_messages([
#     ("system", "너는 지금부터 내 여자친구야. 너는 어릴 때 일진이었고, 그래서 그런지 말을 거칠게 하는 편이야."),
#     ("user", "{input}")
# ])
# chain = prompt | llm 
# result = chain.invoke({"input": "자기야, 오늘은 우리 뭐하고 놀까?"})
# print(result)


# import streamlit as st

# st.title('This is a title')
# st.title('_Streamlit_ is :blue[cool] :sunglasses:')