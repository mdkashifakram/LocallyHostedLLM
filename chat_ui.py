import streamlit as st
from llm_connector import stream_response
from chat_manager import format_chat_history, append_to_history


def clean_response(response: str):
    unwanted_phrase = "I am a language model trained by Mistral AI. I'm here to assist you with your questions and tasks. How can I help you further today?"
    return response.replace(unwanted_phrase, "").strip()

st.set_page_config(page_title="LLMChat-Local_V0.1", layout="centered")

st.title("LLMChat-Local_V1.3")
st.markdown("Ask me anything!")
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
for chat in st.session_state.chat_history:
    with st.container():
        if chat["role"] == "user":
            st.markdown(f"<div style='text-align: right; background-color: #e0f7fa; padding: 8px 15px; border-radius: 15px; max-width: 80%; margin: 5px auto; word-wrap: break-word;'>"
                        f"{chat['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='text-align: left; background-color: #f1f1f1; padding: 8px 15px; border-radius: 15px; max-width: 80%; margin: 5px auto; word-wrap: break-word;'>"
                        f"{chat['content']}</div>", unsafe_allow_html=True)
if len(st.session_state.chat_history) == 0:
    st.session_state.chat_history.append({"role": "assistant", "content": ""})
if user_prompt := st.chat_input("Type your message here..."):
    append_to_history(st.session_state.chat_history, "user", user_prompt)
    st.markdown(f"<div style='text-align: right; background-color: #e0f7fa; padding: 8px 15px; border-radius: 15px; max-width: 80%; margin: 5px auto; word-wrap: break-word;'>"
                f"{user_prompt}</div>", unsafe_allow_html=True)
    with st.container():
        response_area = st.empty()
        full_response = ""
        prompt = format_chat_history(st.session_state.chat_history)

        for chunk in stream_response(prompt):
            full_response += chunk
            cleaned_response = clean_response(full_response)
            response_area.markdown(f"<div style='text-align: left; background-color: #f1f1f1; padding: 8px 15px; border-radius: 15px; max-width: 80%; margin: 5px auto; word-wrap: break-word;'>"
                                   f"{cleaned_response}</div>", unsafe_allow_html=True)
        cleaned_response = clean_response(full_response)
        response_area.markdown(f"<div style='text-align: left; background-color: #f1f1f1; padding: 8px 15px; border-radius: 15px; max-width: 80%; margin: 5px auto; word-wrap: break-word;'>"
                               f"{cleaned_response}</div>", unsafe_allow_html=True)
        append_to_history(st.session_state.chat_history, "assistant", cleaned_response)
