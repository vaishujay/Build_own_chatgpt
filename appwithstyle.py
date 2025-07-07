import streamlit as st
from callollama import callOLLAMA

# --- Page config ---
st.set_page_config(page_title="🧠 Ollama Chatbot", layout="centered")

# --- Custom CSS Styling ---
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .stChatMessage {
        padding: 0.5rem;
        border-radius: 1rem;
        margin-bottom: 1rem;
    }

    .stChatMessage[data-testid="stChatMessage"][data-streamlit-chat-message-role="assistant"] {
        background-color: #f0f8ff;
        border-left: 5px solid #007acc;
    }

    .stChatMessage[data-testid="stChatMessage"][data-streamlit-chat-message-role="user"] {
        background-color: #e6ffe6;
        border-right: 5px solid #33cc33;
        text-align: right;
    }

    input[type="text"] {
        font-size: 16px !important;
        padding: 0.6rem;
        border-radius: 0.5rem;
        border: 1px solid #ccc;
    }

    button[kind="primary"] {
        background-color: #007acc !important;
        color: white !important;
        font-weight: bold;
        border-radius: 0.5rem;
        padding: 0.4rem 1.2rem;
        margin-top: 0.5rem;
    }

    .stButton>button {
        background-color: #ff6666 !important;
        color: white !important;
        font-weight: bold;
        border-radius: 0.5rem;
    }

    .stSpinner {
        color: #007acc;
    }
</style>
""", unsafe_allow_html=True)

# --- Initialize session state ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hello! I am your Smart Offline Chatbot. Ask me anything!"}
    ]
if "is_typing" not in st.session_state:
    st.session_state.is_typing = False

# --- Page Header ---
st.markdown("<h1 style='text-align: center;'>🧠 Offline LLM Chatbot</h1>", unsafe_allow_html=True)
st.markdown("### 🤖 Session 2: Offline GPT Interaction")
st.markdown("---")

# --- Chat History Display ---
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user", avatar="image/user_icon.png"):
            st.markdown(message["content"])
    else:
        with st.chat_message("assistant", avatar="image/bot_icon.png"):
            st.markdown(message["content"])

# --- Typing Indicator ---
if st.session_state.is_typing:
    with st.chat_message("assistant", avatar="image/bot_icon.png"):
        with st.spinner("Typing..."):
            st.empty()

# --- Input Area ---
st.markdown("---")
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("💬 Type your message:", placeholder="Ask me anything...")
    send_button = st.form_submit_button("🚀 Send")

# --- Clear Button ---
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# --- Handle User Input ---
if send_button and user_input.strip():
    st.session_state.messages.append({"role": "user", "content": user_input.strip()})
    st.session_state.is_typing = True
    st.rerun()

# --- Process Bot Response ---
if st.session_state.is_typing:
    user_message = st.session_state.messages[-1]["content"]
    with st.chat_message("assistant", avatar="image/bot_icon.png"):
        with st.spinner("Typing..."):
            bot_response = callOLLAMA(user_message)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.session_state.is_typing = False
    st.rerun()
