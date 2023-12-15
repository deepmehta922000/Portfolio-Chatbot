# Q&A Chatbot
from langchain.llms import OpenAI
import streamlit as st
import time

# Function to load OpenAI model and get responses
def get_openai_response(question, resume_summary):
    # Concatenate resume details with the user's input
    input_prompt = f"{resume_summary}\n\nUser Question: {question}"

    llm = OpenAI(model_name="text-davinci-003", temperature=0.5)
    response = llm(input_prompt)
    return response

# Initialize streamlit app
st.set_page_config(page_title="Deep Portfolio Bot")
st.title("Chatbot")

st.text("Please wait 20 seconds after each question as I am using the free version of OPENAI API. Thank you for your patience.")

# Read resume information from the text file
with open("resume.txt", "r", encoding="utf-8") as file:
    resume_summary = file.read()

# Initialize history list
history = []

# Text input for user question
input_question = st.text_input("Ask a question about Deep Mehta:", key="input")

# Get response for the current question
response = get_openai_response(input_question, resume_summary)

# Button to ask the question
submit = st.button("Ask the question")

# If the ask button is clicked
if submit:
    # Append the current question and response to history
    history.append({"question": input_question, "response": response})

    # Introduce a 20-second timer
    st.info("Waiting for 20 seconds before the next question...")
    time.sleep(20)  # Sleep for 20 seconds

# Display history
st.subheader("Chat History:")
for item in history:
    st.write(f"**Question:** {item['question']}")
    st.write(f"**Response:** {item['response']}")
    st.write("---")  # Add a separator between questions and responses
