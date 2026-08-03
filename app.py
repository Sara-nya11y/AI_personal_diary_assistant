import streamlit as st
from groq import Groq

api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

st.set_page_config(page_title="AI Personal Diary Assistant", page_icon="✨")
st.title("✨ AI Personal Diary Assistant")
st.write("Tell me your task and mood, I'll create a 5-point plan for you")
