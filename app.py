import streamlit as st
from groq import Groq
import os


# Load API Key

import streamlit as st
from groq import Groq

# IDI KOTHADI - BOTH WAYS CHECK CHESTHUNDI
try:
    api_key = st.secrets["GROQ_API_KEY"]
except:
    api_key = st.secrets.get("GROQ_API_KEY")

client = Groq(api_key=api_key)

# Page Setup
st.set_page_config(page_title="AI Personal Diary Assistant", page_icon="✨")
st.title("✨ AI Personal Diary Assistant")
st.write("Tell me your task and mood, I'll create a 5-point plan for you")

# Input Section
st.header("Tell me about your day")
task = st.text_input("1. What is your main task today?")
time = st.text_input("2. How much time do you have? Example: 2 hours")
mood = st.selectbox("3. How are you feeling?", ["Motivated", "Stressed", "Lazy", "Confused", "Excited"])

# Generate Button
if st.button("Generate Plan ✨"):
    if task == "" or time == "":
        st.warning("Please fill Task and Time")
    else:
        with st.spinner("AI is creating your plan..."):
            prompt = f"""
You are a friendly English assistant.
Student details:
Main Task: {task}
Available Time: {time}
Mood: {mood}

Based on this, give me a 5 point simple, practical daily plan.
Write ONLY in clear ENGLISH. Use bullet points. Be motivating.
"""

            try:
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                plan = response.choices[0].message.content
                st.success("✅ Your plan is ready!")
                st.write(plan)
            except Exception as e:
                st.error(f"Error: {e}")
