# Smart Calorie Meter & Adviser

This application acts as a nutritionist AI assistant. It analyzes images containing food items and provides detailed information about the calorie content, nutrients, and overall healthiness of the meal. The app uses the Google Generative AI (Gemini-Pro Vision) model to process the image and generate a comprehensive response.

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
streamlit run nutritionist.py
```

3. The app will open in your default web browser. If it doesn't open automatically, you can access it by clicking the URL provided in the terminal.

## Usage

1. Upload an image containing food items by clicking the "Choose an Image of the Invoice" button and selecting a JPG, JPEG, or PNG file.
2. Click the "Tell me about the Calories" button.
3. The application will analyze the image and provide the following information:
   - List of food items present in the image
   - For each food item:
     - Item name
     - Number of calories per serving
     - Brief description, including key nutrients
   - Analysis of the overall meal (healthy or unhealthy)
   - Approximate percentage breakdown of carbohydrates, fats, fiber, protein, and sugar in the meal
   - Recommended daily intake amounts for each nutrient category

## Image Sections
![Screenshot 2024-05-28 174210](https://github.com/majisouvik26/GEN-AI-Projects/assets/153885959/ce26fab1-d67f-495d-8158-703b1d2166c9)

![Screenshot 2024-05-28 174258](https://github.com/majisouvik26/GEN-AI-Projects/assets/153885959/7014db75-71f7-4f54-bb96-f5da11b2f94b)
