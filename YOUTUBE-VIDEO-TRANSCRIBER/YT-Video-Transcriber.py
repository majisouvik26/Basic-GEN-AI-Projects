from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt="""You are a YouTube Video Summarizer. Your task is to take the transcript text of a YouTube video and provide a concise and comprehensive summary. The summary should highlight the key points and main ideas presented in the video. Focus on capturing the essence of the content in a clear and coherent manner. The summary should be presented in bullet points and should not exceed 250 words. Your goal is to make the summary informative and easy to understand, allowing readers to grasp the core message of the video quickly. Please ensure that the summary is accurate and reflects the primary themes and topics discussed. The transcript text will be appended here, and you will use it to extract the most relevant information. Aim to provide a balanced summary that covers all major aspects of the video, avoiding unnecessary details or repetitive information. This will help viewers who may not have the time to watch the entire video but still want to understand its main points. Please provide the summary here : """

def extract_transcript(url):
    try:
        video_id = url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)
        
        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]
        return transcript
      

    
    except Exception as e:
        st.error("An error occurred while retrieving the transcript.")
        return None

        

def get_content(transcript_text,prompt):
    model=genai.GenerativeModel("gemini-pro")
    res=model.generate_content(prompt+transcript_text)
    return res.text

st.title("Youtube Video Transcriber")
url=st.text_input("Enter Youtube link here: ")

if url:
    id= url.split("=")[1]
    st.image(f"https://img.youtube.com/vi/{id}/0.jpg", use_column_width=True)
    
if st.button("Get Detailed Transcript"):
    text=extract_transcript(url)
    
    if text:
        summary = get_content(text,prompt)
        st.markdown("Transcript: ")
        st.write(summary)
        
    