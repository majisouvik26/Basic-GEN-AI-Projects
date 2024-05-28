# English YouTube Video Transcriber

This application allows you to transcribe and summarize the content of an English YouTube video. It uses the YouTube Transcript API to extract the transcript text and the Google Generative AI (Gemini-Pro) model to generate a concise and comprehensive summary of the video's content.

## Live Demo

You can access the live demo of this application on Hugging Face Spaces: [https://huggingface.co/spaces/souvikmaji22/English-Youtube-Video-Transcriber](https://huggingface.co/spaces/souvikmaji22/English-Youtube-Video-Transcriber)

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

## Running the App

1. Make sure your virtual environment is activated.

2. Run the Streamlit app using the following command:

```
streamlit run app.py
```

3. The app will open in your default web browser. If it doesn't open automatically, you can access it by clicking the URL provided in the terminal.

## Usage

1. Enter the YouTube video link in the input field.
2. Click the "Get Detailed Transcript" button.
3. The application will display a thumbnail image of the video.
4. The generated summary of the video's content will be displayed below.

## Image Sections
![Screenshot 2024-05-28 171509](https://github.com/majisouvik26/GEN-AI-Projects/assets/153885959/4bad1524-3a38-4d09-a55d-793e5043a90c)
