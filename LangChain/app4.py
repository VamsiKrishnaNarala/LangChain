import os
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from key import openapi_key
import streamlit as st


os.environ["OPENAI_API_KEY"]=openapi_key

st.title("CHATBOT")
input_text=st.text_input("Enter Topic You Want")


#PRompt Template-1

first_input_text=PromptTemplate(
    input_variables=['name'],
    template='Tell me About {name}'
)


#OpenAI LLM
llm=OpenAI(temperature=0.8)

chain=LLMChain(llm=llm,prompt=first_input_text,verbose=True,output_key='title')

#Prompt Template-2


second_input_text=PromptTemplate(
    input_variables=['title'],
    template='When Was {name} Born'
)


chain2=LLMChain(llm=llm,prompt=second_input_text,verbose=True,output_key='dob')


third_input_text=PromptTemplate(
    input_variables=['dob'],
    template='Major Events on {dob} '
)


chain3=LLMChain(llm=llm,prompt=third_input_text,verbose=True,output_key='des')


Parent_chain=SequentialChain(
    chains=[chain,chain2,chain3],
    input_variables=['name'],
    output_variables=['title','dob','des'],
    verbose=True)

if input_text:
    st.write(Parent_chain({'name':input_text}))