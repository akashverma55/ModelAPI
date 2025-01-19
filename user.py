# |===================Importing the Libraries=======================|

import streamlit as st
import requests

# |=================================================================|

# |===============Function for calling the API======================|

def get_llm1_response(input_text):
    response = requests.post("http://localhost:8000/explanation/invoke",
                            json = {'input':{'topic':input_text}})

    return response.json()['output']

def get_llm2_response(input_text):
    response = requests.post("http://localhost:8000/adv&disadv/invoke",
                            json = {'input':{'topic':input_text}})

    return response.json()['output']

# |=================================================================|

# |===================Streamlit Framework===========================|

st.title('Langchain Demo with QWEN API chains')
input_text1 = st.text_input("Ask about any topic.")

if input_text1:
    st.write(get_llm1_response(input_text1))

input_text2 = st.text_input("Type the topic name for its advantages and disadvantages.")

if input_text2:
    st.write(get_llm2_response(input_text2))

# |=================================================================|