# Q&A Chatbot
from langchain.llms import OpenAI
import streamlit as st
import time

# Function to load OpenAI model and get responses
def get_openai_response(question, resume_summary):
    try:
        # Concatenate resume details with the user's input
        input_prompt = f"{resume_summary}\n\nUser Question: {question}"

        llm = OpenAI(model_name="text-davinci-003", temperature=0.5)
        response = llm(input_prompt)
        return response
    except Exception as e:
        error_message = f"An error occurred. Please refresh the page. Error details: {e}"
        return error_message

# Initialize streamlit app
st.set_page_config(page_title="Deep Portfolio Bot")
st.title("Chatbot")

# Adjusted display text
st.markdown("### Welcome to the Chatbot")
st.markdown("Please wait 20 seconds after each question as I am using the free version of OPENAI API. Thank you for your patience.")

# Read resume information from the text file
with open("resume.txt", "r", encoding="utf-8") as file:
    resume_summary = file.read()

# Text input for user question
input_question = st.text_input("Ask a question about Deep Mehta:", key="input")

# Get response for the current question
response = get_openai_response(input_question, resume_summary)

# Button to ask the question
submit = st.button("Ask the question")

# If the ask button is clicked
if submit:
    # Display the response immediately
    st.subheader("Response:")
    st.write(response)
    # Introduce a 20-second timer
    timer_placeholder = st.empty()
    for remaining_time in range(20, 0, -1):
           timer_placeholder.text(f"Please wait for {remaining_time} seconds before the next question...")
           time.sleep(1)  # Sleep for 1 second

    timer_placeholder.success("Next question available!")
