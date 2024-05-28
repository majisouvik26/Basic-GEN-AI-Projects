# ATS Tracker App

The ATS Tracker App is a smart resume assistant that evaluates resumes against job descriptions using the Google Generative AI (Gemini-Pro Vision) model. It provides a percentage match, identifies missing keywords, and offers a profile summary to help improve your resume.

## Clone the Repository

To get started, you'll need to clone the repository to your local machine:

```sh
git clone https://github.com/majisouvik26/GEN-AI-Projects.git
```

## Prerequisites

Before running the app, you need to set up a virtual environment and install the required dependencies. For example, you can follow these steps:

1. Install Anaconda or Miniconda if you haven't already.

2. Create a new virtual environment with Python 3.10:

```sh
conda create -p venv python=3.10 -y
```

3. Activate the virtual environment:

```sh
conda activate venv
```

4. Install the required dependencies from the `requirements.txt` file:

```sh
pip install -r requirements.txt
```

## Environment Setup

1. Create a `.env` file in the project directory and add your Google API key:

```sh
GOOGLE_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your actual Google API key.

## Running the App

1. Make sure your virtual environment is activated.

2. Run the Streamlit app using the following command:

```sh
streamlit run ATS-tracker.py
```

3. The app will open in your default web browser. If it doesn't open automatically, you can access it by clicking the URL provided in the terminal.

## Usage

1. Enter the job description in the provided text area.
2. Upload your resume in PDF format by clicking the "Upload Your Resume" button.
3. Click the "Submit here" button.
4. The application will analyze your resume and provide the following information:
   - Job Description Match Percentage
   - Missing Keywords
   - Profile Summary
