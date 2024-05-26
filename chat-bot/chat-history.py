from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_repsonse(qs):
    res = chat.send_message(qs,stream=True)
    return res

st.set_page_config(page_title="Q&A")
st.header("Gemini Pro LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] =[]
    
input=st.text_input("Input: ", key="input")
submit=st.button("Ask your question here")

if submit and input:
    response=get_repsonse(input)
    st.session_state['chat_history'].append(("You",input))
    st.subheader("The response is: ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot",chunk.text))
        
st.subheader("Chat History: ")

for r,t in st.session_state['chat_history']:
    st.write(f"{r}:{t}") # r-> bot/user t->text