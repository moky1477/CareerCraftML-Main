import streamlit as st
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit as st
from dotenv import load_dotenv

# Load dotenv before importing other modules
load_dotenv()

# Import os for environment variables
import os

# Replace 'gemini_library' with the correct library for Google Gemini
import google.generativeai as genai 

# Assuming 'gemini_library' has a 'GenerativeModel' class
# Replace 'google.generativeai' with the actual library for Google Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video, providing the important summary in points
within 500 words. Please provide the summary of the text given here:  """

# Function to get the transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

# Function to generate the summary based on Prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    # Replace 'GenerativeModel' and 'generate_content' with the actual methods from the gemini library
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        # Pass correct arguments to the generate_gemini_content function
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
