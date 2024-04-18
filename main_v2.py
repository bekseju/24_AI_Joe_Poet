# Version 2 - streamlit 업로드 서버 실행

# from dotenv import load_dotenv
# load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI()

# streamlit 실행방법 : streamlit run main_v1.py
import streamlit as st


st.title('인공지능 시인')

# content = "코딩"
content = st.text_input('시의 주제를 제시해주세요')
st.write('시의 주제는', content)

# if st.button('Say hello'):
#     st.write('Why hello there')

# result = llm.invoke(content + "에 대한 시를 써줘")
# print(result)

if st.button("시 작성 요청하기"):
    with st.spinner('시 작성 중...'):
        result = llm.invoke(content + "에 대한 시를 써줘. 시는 조선시대 시조 형태로 작성해줘.").content
    st.write(result)

# from langchain_core.messages import AIMessage
# AIMessage.content