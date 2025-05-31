import streamlit as st
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPEN_AI_API")  # Replace with your key for local testing

# Streamlit app
st.title("Chatbot with Streamlit")
st.sidebar.header("Settings")

# Sidebar input for API key (optional, for secure handling)
user_api_key = st.sidebar.text_input("", type="password")
if user_api_key:
    openai.api_key = user_api_key

# User input
user_input = st.text_input("Ask me anything:")

# Chatbot response
if st.button("Send"):
    if not openai.api_key:
        st.error("API key not found. Please provide your OPENAI API key in the settings.")
    elif user_input.strip() == "":
        st.warning("Please enter a question or prompt.")
    else:
        try:
            response = client.chat.completion.create(
                model="gpt-3.5-turbo",  
                messages=[{"role": "user", "content": user_input}],
                max_tokens=150
            )
            answer = response["choices"][0]["message"]["content"].strip()
            st.success(f"Chatbot: {answer}")
        except Exception as e:
            st.error(f"An error occurred: {e}")

st.sidebar.write("Developed with ❤️ using Streamlit")
