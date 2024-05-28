# Document Q&A using Gemma

This application allows you to ask questions and get answers based on the context of documents in a specified directory. It uses the Langchain library, the ChatGroq model (Gemma-7b-it), and the Google Generative AI Embeddings to process the documents, create embeddings, and retrieve relevant information to answer your questions.

## Clone the Repository

To get started, you'll need to clone the repository to your local machine:

```
git clone https://github.com/majisouvik26/GEN-AI-Projects.git
```

## Prerequisites

Before running the app, you need to set up a virtual environment and install the required dependencies. For example, you can follow these steps:

1. Install Anaconda or Miniconda if you haven't already.

2. Create a new virtual environment with Python 3.10:

```
conda create -p venv python=3.10 -y
```

3. Activate the virtual environment:

```
conda activate venv
```

4. Install the required dependencies from the `requirements.txt` file:

```
pip install -r requirements.txt
```

## Environment Setup

1. Create a `.env` file in the project directory and add your GroQ API key and Google API key:

```
GROQ_API_KEY=your_groq_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

Replace `your_groq_api_key_here` and `your_google_api_key_here` with your actual API keys.

## Datasets

The application looks for documents in the `./datasets` directory. You can place your own PDF files in this directory, and the application will process them. If you want to use a different directory, modify the `PyPDFDirectoryLoader` line in the `embeddings()` function to point to your desired directory.

## Running the App

1. Make sure your virtual environment is activated.

2. Run the Streamlit app using the following command:

```
streamlit run document-QA.py
```

3. The app will open in your default web browser. If it doesn't open automatically, you can access it by clicking the URL provided in the terminal.

## Usage

1. Click the "Create Vector Store" button to process the documents in the `./datasets` directory and create embeddings.
2. Enter your question in the text input field.
3. The application will search the document embeddings, retrieve relevant context, and display the answer to your question.
4. You will get "Document Similarity Search" section to view the relevant document excerpts.
