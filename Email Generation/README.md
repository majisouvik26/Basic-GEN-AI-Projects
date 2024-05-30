# Email Generator App

This is a Streamlit app that generates email messages based on the style and details provided by the user. It utilizes the Llama-2-7B-Chat-GGML language model from CTransformers for generating the email content.

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

## Running the App

1. Make sure your virtual environment is activated.

2. Run the Streamlit app using the following command:

```
streamlit run email.py
```

3. The app will open in your default web browser. If it doesn't open automatically, you can access it by clicking the URL provided in the terminal.

## Usage

1. Enter the email subject in the text area provided.
2. Enter the sender's name in the "Sender Name" input field.
3. Enter the recipient's name in the "Recipient Name" input field.
4. Select the desired writing style (Formal, Appreciating, Not Satisfied, or Neutral) from the dropdown menu.
5. Click the "Generate" button to generate the email content based on the provided inputs.
6. The generated email will be displayed in the app.

## Image Sections
![Screenshot 2024-05-31 000648](https://github.com/majisouvik26/GEN-AI-Projects/assets/153885959/89498082-353f-4022-99d9-da5c1fd11598)


![Generated Email](https://i.imgur.com/YourImageURL.png)

Note: Replace `https://i.imgur.com/YourImageURL.png` with the actual image URLs for your project.

That's it! You now have a README file that covers cloning the repository, prerequisites, environment setup, running the app, usage, and includes placeholders for images related to the email generation interface and the generated email. Don't forget to replace the image URLs with your actual image URLs.
