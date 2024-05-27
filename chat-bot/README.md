# Gemini Pro Chat Application

This is a chat application built using Streamlit and the Google Generative AI (Gemini Pro) model. The app allows users to have a conversation with the Gemini Pro model, where the chat history is maintained and displayed in the app.

## Clone the Repository

To get started, you'll need to clone the repository to your local machine:

```
git clone https://github.com/majisouvik26/GEN-AI-Projects.git
```

## Prerequisites

Before running the app, you need to set up a virtual environment and install the required dependencies. For example, you can follow these steps:

1. Install Anaconda or Miniconda if you haven't already.

2. Create a new virtual environment with Python 3.9:

```
conda create -p venv python=3.9 -y
```

3. Activate the virtual environment:

```
conda activate venv
```

4. Install the required dependencies from the `requirements.txt`(you can find this file [here]([https://huggingface.co/spaces/souvikmaji22/lfw_face_recognition](https://github.com/majisouvik26/GEN-AI-Projects/blob/main/requirements.txt))) file:

```
pip install -r requirements.txt
```

## Environment Setup

1. Create a `.env` file in the project directory and add your Google API key:

```
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Google API key.

## Running the App

1. Make sure your virtual environment is activated.

2. Run the Streamlit app using the following command:

```
streamlit run chat-history.py
```

3. The app will open in your default web browser. If it doesn't open automatically, you can access it by clicking the URL provided in the terminal.

## Usage

1. Enter your message in the input field.
2. Click the "Ask your question here" button to send the message.
3. The response from the Gemini Pro model will be displayed below.
4. The chat history, including your messages and the model's responses, will be displayed at the bottom of the app.

## Image Sections

### Chat Interface
![Chat Inference](https://github.com/majisouvik26/GEN-AI-Projects/assets/153885959/409517c2-3f79-4297-98de-9968f33acc7f)

### Chat History
![Chat History](https://github.com/majisouvik26/GEN-AI-Projects/assets/153885959/52f9902a-5bfb-4ea4-87e6-b71fddd916eb)


