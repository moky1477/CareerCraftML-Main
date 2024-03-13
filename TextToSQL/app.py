from dotenv import load_dotenv
import os
import streamlit as st
import sqlite3
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])

    return response.text

# Function to retrieve query from the SQL database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Define Your Prompt
prompt = """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
SECTION, and MARKS. For example,
Example 1 - How many entries of records are present?,
the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
Example 2 - Tell me all the students studying in Data Science class?,
the SQL command will be something like this SELECT * FROM STUDENT
where CLASS="Data Science";
also, the SQL code should not have ``` in the beginning or end and sql word in output
"""

## Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    st.subheader("The Response is")
    st.write(response)
    
    # Attempt to execute the SQL query
    try:
        sql_result = read_sql_query(response, "student.db")
        st.table(sql_result)
    except sqlite3.Error as e:
        st.error(f"Error executing SQL query: {str(e)}")
