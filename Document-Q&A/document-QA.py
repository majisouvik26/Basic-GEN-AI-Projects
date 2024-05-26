import os
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader


from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY']=os.getenv("GOOGLE_API_KEY")

st.title("Document Q&A using Gemma")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="Gemma-7b-it")

#print(llm)

prompt=ChatPromptTemplate.from_template(
"""
Answer the following questions using only the given context. Provide the most accurate responses based on the context provided.

<context>
{context}
<context>
Questions: {input}

"""
)

def embeddings():
    if "vectors" not in st.session_state:
        st.session_state.embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader=PyPDFDirectoryLoader("./datasets")
        st.session_state.docs=st.session_state.loader.load()
        st.session_state.text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=2000)
        st.session_state.final_documents=st.session_state.text_splitter.split_documents(st.session_state.docs)
        st.session_state.vectors=FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)
        

prompt1=st.text_input("Ask something from the documents")

if st.button("Create Vector Store"):
    embeddings()
    st.write("Vector Store DB is Connected")
    
import time

if prompt1:
    document_chain=   create_stuff_documents_chain(llm,prompt)
    retriever= st.session_state.vectors.as_retriever()
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    
    start=time.process_time()
    response=retrieval_chain.invoke({'input':prompt1})
    st.write(response['answer'])
    print(start)
    
    with st.expander("Document Similarity Search"):
        for i,d in enumerate(response["context"]):
            st.write(d.page_content)
            st.write("---------------")