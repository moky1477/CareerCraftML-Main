import streamlit as st
import google.generativeai as genai

import os
from dotenv import load_dotenv
load_dotenv()

import PyPDF2 as pdf 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Pro response
def get_gemini_response(input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(input)
    return response.text

def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text

input_prompt = """
**Job Description Evaluation:**

As a highly advanced Application Tracking System (ATS) specializing in the tech field, software engineering, 
data science, data analysis, and big data engineering, your role is to meticulously evaluate resumes in a fiercely competitive job market. 
Provide the best assistance possible for resume enhancement, assigning a percentage match based on the 
job description (JD) and identifying missing keywords with utmost accuracy.

**Instructions:**
Evaluate the provided resume against the given JD and deliver a comprehensive response in the following format:

**Evaluation Summary:**

- **JD Match:** [%]\n
- **Missing Keywords:** []\n
- **Profile Summary:** ""\n

"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd=st.text_area("Paste the Job Description")
uploaded_file=st.file_uploader("Upload Your Resume",type="pdf",help="Please uplaod the pdf")

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text=input_pdf_text(uploaded_file)
        response = get_gemini_response(input_prompt)
        st.subheader(response)




