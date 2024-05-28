# SQL Query Retrieval

This application allows you to ask questions in natural language and retrieve data from a SQLite database. It uses the Google Generative AI (Gemini-Pro) model to convert your question into an SQL query and then executes that query on the database to fetch the relevant data.

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

1. Create a `.env` file in the project directory and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Google API key.

## Database Setup

The `sql.py` file included in the repository creates a SQLite database named `mall1.db` with sample data. You can use this database for testing purposes or create your own database by modifying the `sql.py` file.

If you want to use your own database, ensure that you update `sql-app.py` correctly, especially the prompt.

## Running the App

1. Make sure your virtual environment is activated.

2. Run the Streamlit app using the following command:

```
streamlit run sql-app.py
```

3. The app will open in your default web browser. If it doesn't open automatically, you can access it by clicking the URL provided in the terminal.

## Usage

1. Enter your question or query in the input field.
2. Click the "Ask your question here" button.
3. The application will convert your question into an SQL query, execute it on the database, and display the results below.
