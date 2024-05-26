import google.generativeai as genai
import os

import streamlit as st
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def res(input_prompt,image):
    model=genai.GenerativeModel('gemini-pro-vision')
    res=model.generate_content([input_prompt,image[0]])
    return res.text
def setup(file):
    if file is not None:
        bytes=file.getvalue()
        image_parts=[
            {
                "mime_type": file.type,
                "data": bytes
            }
        ]
        return image_parts # required by gemini pro vision
    else:
        raise FileNotFoundError("No File Uploaded")
    
st.set_page_config("Smart Calorie Meter & Adviser")
st.header("Smart Calorie Meter & Adviser")
file = st.file_uploader("Choose an Image of the Invoice", type=["jpg","jpeg","png"])

image=""
if file is not None:
    image=Image.open(file)
    st.image(image, caption="Uploaded Image: ", use_column_width=True)
    
submit=st.button("Tell me about the Calories")

input_prompt="""
You are a nutritionist AI assistant. When shown an image containing food items, your task is to:

1. Identify and list out all the food items present in the image.
2. For each food item, provide the following details in a numbered list format:
a. Item name
b. Number of calories per serving
c. A brief description of the item, including key nutrients
3. After listing all food items, analyze the overall meal and determine if it is healthy or unhealthy.
4. Calculate and provide the approximate percentage breakdown of carbohydrates, fats, fiber, protein, and sugar in the entire meal.
5. Mention the recommended daily intake amounts for each of those nutrient categories based on general dietary guidelines.

Please note that you will need the image contents provided directly, as you cannot open links or view images yourself.
"""

if submit:
    image_data= setup(file)
    res = res(input_prompt,image_data)
    st.subheader("Response: ")
    st.write(res)