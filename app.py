from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("google_api_key"))

model=genai.GenerativeModel("gemini-1.5-flash")
def get_response(prompt):
    response = model.generate_content(prompt)
    return response.text


st.title("Google Generative AI with Streamlit")
st.set_page_config(page_title="Generative AI application", page_icon=":robot_face:")
st.header("Ask me anything ")
input_text = st.text_input("Enter your question here:",key="input_text")
submit_button = st.button("Submit")
 
if submit_button:
    response = get_response(input_text)
    st.text_area("Response:", value=response, height=500)
