import streamlit as st
from groq import Groq
from datetime import datetime

# Load API Key from Streamlit Secrets
api_key = st.secrets["GROQ_API_KEY"]
client = Groq(api_key=api_key)

st.set_page_config(page_title="AI Personal Diary Assistant", page_icon="📖")

st.title("📖 AI Personal Diary Assistant")
st.write("Write your daily diary and let AI analyse it.")

# Date
today = datetime.now().strftime("%d-%m-%Y")
st.subheader(f"Date: {today}")

diary = st.text_area(
    "Write your diary here...",
    height=250
)

# Save Diary
if st.button("💾 Save Diary"):
    if diary.strip() == "":
        st.warning("Please write something before saving.")
    else:
        with open("diary_entries.txt", "a", encoding="utf-8") as file:
            file.write(f"\n\nDate: {today}\n")
            file.write(diary)
            file.write("\n")
        st.success("Diary saved successfully!")

# AI Analysis
if st.button("🤖 Analyse Diary"):
    if diary.strip() == "":
        st.warning("Please write your diary first.")
    else:
        prompt = f"""
You are an AI Personal Diary Assistant.

Read the diary entry below and provide:
1. Mood
2. Short Summary
3. Three Positive Suggestions

Diary:
{diary}

Output format:
Mood:
Summary:
Suggestions:
"""

        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.5,
                max_tokens=400
            )

            result = response.choices[0].message.content

            st.subheader("📊 AI Analysis")
            st.write(result)

        except Exception as e:
            st.error(f"Error: {e}")