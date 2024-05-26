from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_text(pdfs):
    text = ""
    for pdf in pdfs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vectors(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conv_chain():
    prompt_template = """
    Answer the question as detailed as possible based on the provided context. If the answer is not in the provided context, simply state, "The answer is not in the context." Do not provide incorrect or misleading information.\n\n
    Context:\n {context}?\n
    Question: \n{question}\n
    
    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)
    
    return chain

def user_input(qs):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(qs)
    chain = get_conv_chain()
    
    res = chain(
        {"input_documents": docs, "question": qs}, return_only_outputs=True      
    )
    
    print(res)
    st.write("Response: ", res["output_text"])

# Streamlit

def main():
    st.set_page_config(page_title="Chat with Multiple PDF")
    st.header("Chat with Multiple PDF using Gemini-Pro")
    
    user_qs = st.text_input("Ask a question from your PDF Files")
    
    if user_qs:
        user_input(user_qs)
    with st.sidebar:
        st.title("Menu: ")
        docs = st.file_uploader("Upload your PDF files", type=["pdf"], accept_multiple_files=True)
        
        if st.button("Submit & Proceed"):
            if docs:
                with st.spinner("Please wait a moment..."):
                    t = get_text(docs)
                    text_chunks = get_chunks(t)
                    get_vectors(text_chunks)
                    st.success("Done!")
            else:
                st.warning("Please upload at least one PDF file.")

if __name__ == "__main__":
    main()
