from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")
def get_response(qs):
    response=model.generate_content(qs)
    return response.text

#streamlit app

st.set_page_config(page_title="Q&A")

st.header("Gemini Pro LLM")

input=st.text_input("Input: ",key="input")

submit=st.button("Ask your Question")

if submit:
    response=get_response(input)
    st.subheader("The Response is: ")
    st.write(response)