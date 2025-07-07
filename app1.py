# import streamlit as st
# from datetime import datetime
# import requests
# import json

# st.set_page_config(
#     page_title="Ollama Chatbot", 
#     )

# if "messages" not in st.session_state:
#     st.session_state.messages = []
#     st.session_state.messages.append(
#         {
#             "role": "assistant",
#             "content": "Hello! I am Smart Chatbot, your AI assistant. How can I help you today?"
#         }
#     )


# if "is_typing" not in st.session_state:
#     st.session_state.is_typing = False

# st.title("Offline LLM")
# st.markdown("Welcome to session 2 of offline GPT")

# st.subheader("Chat here")

# for message in st.session_state.messages:
#     if message["role"] == "user":
#         st.info(message["content"])
#     else:
#         st.success(message["content"])

# if st.session_state.is_typing:
#     st.markdown("Bot is typing...")
#     st.warning("Typing...")

# st.markdown("---")
# st.subheader("Your message")

# with st.form(key="chat_form", clear_on_submit=True):
#     user_input = st.text_input(
#         "Type your message here",
#         placeholder="Ask me anything....",
#         )
#     send_button = st.form_submit_button("Send", type="primary")

# col1, col2 = st.columns([1, 1])


# with col1:
#     clear_button = st.button("Clear chat")

# if send_button and user_input.strip():
#     st.session_state.messages.append(
#         {
#             "role": "user",
#             "content": user_input.strip()
#         }
#     )
    
# from callollama import callOLLAMA

# if st.session_state.is_typing:
#     user_message = st.session_state.messages[-1]["content"]
#     bot_response = callOLLAMA(user_message)
#     st.session_state.messages.append(
#         {
#             "role": "assistant",
#             "content": bot_response
#         }
#     )
#     st.session_state.is_typing = False
#     st.rerun()



import streamlit as st
from datetime import datetime
import requests
import json
from callollama import callOLLAMA  # Make sure this is defined correctly

# Page config
st.set_page_config(
    page_title="Ollama Chatbot"
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
        "role": "assistant",
        "content": "Hello! I am Smart Chatbot, your AI assistant. How can I help you today?"
    })

if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

# Page content
st.title("Offline LLM")
st.markdown("Welcome to session 2 of offline GPT")
st.subheader("Chat here")

# Show message history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.info(message["content"])
    else:
        st.success(message["content"])

# Typing indicator
if st.session_state.is_typing:
    st.warning("Bot is typing...")

# Input section
st.markdown("---")
st.subheader("Your message")

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "Type your message here",
        placeholder="Ask me anything..."
    )
    send_button = st.form_submit_button("Send", type="primary")

# Clear chat button
col1, col2 = st.columns([1, 1])
with col1:
    clear_button = st.button("Clear chat")

if clear_button:
    st.session_state.messages = []
    st.experimental_rerun()

# Handle user input
if send_button and user_input.strip():
    st.session_state.messages.append({
        "role": "user",
        "content": user_input.strip()
    })
    st.session_state.is_typing = True
    st.rerun()

# Process bot response AFTER rerun
if st.session_state.is_typing:
    user_message = st.session_state.messages[-1]["content"]
    bot_response = callOLLAMA(user_message)
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })
    st.session_state.is_typing = False
    st.rerun()
