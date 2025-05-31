import streamlit as st
from openai import OpenAI
import os

# Streamlit app
st.title("💬 Chatbot with Streamlit")
st.sidebar.header("🔐 API Settings")

# Get API key from Streamlit secrets or user input
api_key = os.getenv("OPENAI_API_KEY")  # from Streamlit Cloud secrets
user_api_key = st.sidebar.text_input("Enter your OpenAI API Key (optional):", type="password")
if user_api_key:
    api_key = user_api_key  # override if provided manually

if not api_key:
    st.error("❌ No API key provided. Please add it in the sidebar or as a Streamlit secret.")
    st.stop()

# Initialize OpenAI client with the final API key
client = OpenAI(api_key=api_key)

# User input
user_input = st.text_input("Ask me anything:")

# Generate and display response
if st.button("Send"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a question or prompt.")
    else:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}],
                max_tokens=150
            )
            answer = response.choices[0].message.content.strip()
            st.success(f"🤖 Chatbot: {answer}")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")

st.sidebar.markdown("---")
st.sidebar.caption("Made with ❤️ using Streamlit and OpenAI")
