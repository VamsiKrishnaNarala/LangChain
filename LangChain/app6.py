import os
from langchain_community.llms import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain,SequentialChain
from langchain.memory import ConversationBufferMemory
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

#Memory

person_memory=ConversationBufferMemory(input_key='name',output_key='person_history')
dob_memory=ConversationBufferMemory(input_key='title',output_key='title_history')
conv_memory=ConversationBufferMemory(input_key='dob',output_key='dob_history')

#OpenAI LLM
llm=OpenAI(temperature=0.8)

chain=LLMChain(llm=llm,prompt=first_input_text,verbose=True,output_key='title',memory=person_memory)

#Prompt Template-2


second_input_text=PromptTemplate(
    input_variables=['title'],
    template='When Was {name} Born'
)


chain2=LLMChain(llm=llm,prompt=second_input_text,verbose=True,output_key='dob',memory=dob_memory)


third_input_text=PromptTemplate(
    input_variables=['dob'],
    template='Major Events on {dob} '
)


chain3=LLMChain(llm=llm,prompt=third_input_text,verbose=True,output_key='des',memory=conv_memory)


Parent_chain=SequentialChain(
    chains=[chain,chain2,chain3],
    input_variables=['name'],
    output_variables=['title','dob','des'],
    verbose=True)

if input_text:
    st.write(Parent_chain({'name':input_text}))


    with st.expander('Person Name'): 
        st.info(person_memory.buffer)

    with st.expander('Major Events'): 
        st.info(conv_memory.buffer)