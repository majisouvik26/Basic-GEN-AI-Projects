from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# def res(question,prompt):
#     model=genai.GenerativeModel('gemini-pro')
#     response= model.generate_content([prompt,question])
#     return response.text




def read_sql(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows




def res(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

prompt = """
You are an expert in converting English questions to SQL queries for a mall database. The database contains information about stores in the mall, including columns such as STORE_NAME, CATEGORY, LOCATION, FLOOR, OPENING_TIME, CLOSING_TIME, CONTACT_NUMBER, EMAIL, and WEBSITE.

For example:
1. How many entries of records are present?, The SQL command will be something like this SELECT COUNT(*) FROM MALL_RECORD

2. Tell me all stores located on the Ground Floor, The SQL command will be something like this SELECT * FROM MALL_RECORD WHERE FLOOR = 1

3. Find the store with the contact number 1234567890., The SQL command will be something like this SELECT * FROM MALL_RECORD WHERE CONTACT_NUMBER = '1234567890'

4. List all stores in the 'Clothing' category, The SQL command will be something like this SELECT * FROM MALL_RECORD WHERE CATEGORY = 'Clothing';

5. Show me the store with the website 'www.store1.com', The SQL command will be something like this SELECT * FROM MALL_RECORD WHERE WEBSITE = 'www.store1.com';

only something like the below written part will be considered as the command, no other punctuations are required->
SELECT * FROM MALL_RECORD WHERE WEBSITE = 'www.store1.com';
"""


st.set_page_config(page_title="SQL Query Retrieval")
st.header("SQL Query Retrieval")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask your question here")

if submit and input:
    response = res(input, prompt)
    print(response)
    data = read_sql(response, "mall1.db")
    st.subheader("Response: ")
    for row in data:
        print(row)
        st.header(row)
