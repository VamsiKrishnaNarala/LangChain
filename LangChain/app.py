import os
from langchain_community.llms import OpenAI
from key import openapi_key
import streamlit as st


os.environ["OPENAI_API_KEY"]=openapi_key

st.title("CHATBOT")
input_text=st.text_input("Enter Topic You Want")

llm=OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
