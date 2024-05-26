from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
import streamlit as st
import os
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel('gemini-pro-vision')

def get_res(input,image,prompt):
    res=model.generate_content([input,image[0],prompt])
    return res.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts =[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    
    
#streamlit

st.set_page_config("Multi-Language Invoice Extractor")
st.header("Multi-Language Invoice Extractor")
input=st.text_input("Input: ", key="input")
file = st.file_uploader("Choose an Image of the Invoice", type=["jpg","jpeg","png"])

image=""
if file is not None:
    image=Image.open(file)
    st.image(image, caption="Uploaded Image: ", use_column_width=True)
    
submit=st.button("Tell me")

input_prompt="""
ou are an expert in invoice analysis. I will upload an invoice image, and you need to answer any questions I ask based on the details in the image.
"""

if submit:
    image_data= input_image_setup(file)
    res = get_res(input_prompt,image_data,input)
    st.subheader("Response: ")
    st.write(res)