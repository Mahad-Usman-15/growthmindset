import streamlit as st
import random

st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🚀")

st.title("Growth Mindset Challenge")
st.header("🚀 Welcome to your growth journey")

st.header("💪 What's your challenge today?")
user_input = st.text_input("Enter your challenge")

if user_input:
    st.success(f"🔥 Challenge Faced: {user_input} — Keep pushing forward toward your goal!")
else:
    st.warning("🧠 Tell us about the challenge to get started")

st.header("📝 Reflect on your learnings")
ref = st.text_input("Write your reflection:")

if ref:
    st.success(f"💡 Great insight: {ref}")
else:
    st.info("⚙️ Every experience gives you a lesson!")

st.header("🏆 Celebrate your achievements")
achievements = st.text_input("Share your achievements:")

if achievements:
    st.success(f"🎉 You achieved: {achievements}")
else:
    st.info("🎯 Every small success is a step toward a bigger goal")

motivations = [
    "🌟 Believe in yourself and all that you are.",
    "🌅 Every day is a new beginning. Take a deep breath and start again.",
    "💪 Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "⏰ Don’t watch the clock; do what it does. Keep going.",
    "🚀 Dream big. Start small. Act now.",
    "❌ Doubt kills more dreams than failure ever will.",
    "🧠 Your only limit is your mind.",
    "🔥 Push yourself, because no one else is going to do it for you."
]

if st.button("💬 Click to get Motivation"):
    random_motivation = random.choice(motivations)
    st.success(random_motivation)

 