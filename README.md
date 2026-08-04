# 📖 AI Personal Diary Assistant

> "Turn your daily thoughts into AI-powered insights"

## 📌 Project Overview
AI Personal Diary Assistant is a Streamlit-based web application that helps users maintain a digital diary. The application uses the **Groq LLM API** with **Llama 3.3 70B Versatile** to analyse diary entries, detect the user's mood, generate a summary, and provide positive suggestions.

---

## 🎯 Problem Statement
People often write daily journals but find it difficult to understand their emotional patterns and get actionable feedback. Reading old diaries and finding patterns is time-consuming. 

This project solves that by using Artificial Intelligence to instantly analyse diary entries and provide meaningful insights to improve mental well-being and self-awareness.

---

## ✨ Key Features
- **📝 Write Daily Diary Entries** - Clean and distraction-free text editor
- **💾 Auto Save with Timestamp** - All entries saved with date and time in `diary_entries.txt`
- **😊 AI Mood Detection** - Detects emotions like Happy, Sad, Stressed, Motivated, Anxious etc
- **📄 AI-generated Summary** - Converts long paragraphs into 2-3 line summary
- **💡 Positive Suggestions** - Get 3 personalized actionable tips to improve your day
- **📅 Date-wise Recording** - Track and read old entries easily
- **📱 Responsive Design** - Works on mobile, tablet, and desktop
- **🤖 Powered by Groq LLM** - Ultra-fast AI responses using Llama 3.3 70B

---

## 🛠️ Technologies Used
| Technology | Purpose |
| --- | --- |
| **Python 3.9+** | Core programming language |
| **Streamlit** | Web app frontend and UI framework |
| **Groq API** | AI/LLM for analysis and suggestions |
| **Llama 3.3 70B** | The LLM model used for understanding text |
| **python-dotenv** | Secure API key management for local development |

---

## 📂 Project Structure


---

## 📊 System Architecture / Block Diagram

```mermaid
flowchart TD
    A[User Writes Diary] --> B[Streamlit UI]
    B --> C[Python app.py]
    C --> D[Groq API<br>Llama 3.3 70B]
    D --> E[AI Analysis]
    E --> F[Mood + Summary + 3 Suggestions]
    C --> G[Save to diary_entries.txt]