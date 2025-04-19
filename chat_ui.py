# chat_ui.py
import streamlit as st
from llm_connector import stream_response
from chat_manager import format_chat_history, append_to_history

st.set_page_config(page_title="Zypher-101", layout="centered")

st.title("Zypher-101")
st.markdown("Ask me anything!")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat
for chat in st.session_state.chat_history:
    with st.chat_message("user" if chat["role"] == "user" else "assistant"):
        st.markdown(chat["content"])

# User input
if user_prompt := st.chat_input("Type your message here..."):
    # Add user input to history
    st.chat_message("user").markdown(user_prompt)
    append_to_history(st.session_state.chat_history, "user", user_prompt)

    # Stream response
    with st.chat_message("assistant"):
        response_area = st.empty()
        full_response = ""
        prompt = format_chat_history(st.session_state.chat_history)

        for chunk in stream_response(prompt):
            full_response += chunk
            response_area.markdown(full_response + "▌")

        append_to_history(st.session_state.chat_history, "assistant", full_response)
