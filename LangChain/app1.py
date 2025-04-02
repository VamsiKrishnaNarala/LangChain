import os
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from key import openapi_key
import streamlit as st


os.environ["OPENAI_API_KEY"]=openapi_key

st.title("CHATBOT")
input_text=st.text_input("Enter Topic You Want")


#PRompt Template


first_input_text=PromptTemplate(
    input_variables=['name'],
    template='Tell me About {name}'
)


#OpenAI LLM
llm=OpenAI(temperature=0.8)

chain=LLMChain(llm=llm,prompt=first_input_text,verbose=True)

if input_text:
    st.write(chain.run(input_text))