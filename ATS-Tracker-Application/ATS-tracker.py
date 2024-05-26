import google.generativeai as genai
import os
import PyPDF2 as pdf
import streamlit as st
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def res(input):
    model = genai.GenerativeModel('gemini-pro')
    res = model.generate_content(input)
    return res.text

def input_pdf_text(file):
    reader = pdf.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

input_prompt_template = """
Hey, act like a skilled ATS with a deep understanding of the tech field, including software engineering, data science, data analysis, and big data engineering. Your task is to evaluate the resume based on the provided job description. Consider that the job market is highly competitive, and provide the best possible assistance to improve the resume. Assign a percentage match based on the job description and identify any missing keywords with high accuracy.

resume: {resume_text}
description: {job_description}

I want the response in a single string structured as:
{{"Job Description Match": "%", "Missing Keywords": [], "Profile Summary": ""}}
"""

st.title("ATS Tracker App")
st.text("Your Smart Resume Assistant")

job_description = st.text_area("Write Your Job Description")
file = st.file_uploader("Upload Your Resume", type="pdf", help="Please Upload the PDF")

submit = st.button("Submit here")
if submit:
    if file is not None:
        resume_text = input_pdf_text(file)
        input_prompt = input_prompt_template.format(resume_text=resume_text, job_description=job_description)
        response = res(input_prompt)
        st.subheader(response)
