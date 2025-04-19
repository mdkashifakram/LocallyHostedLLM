def format_chat_history(history):
    formatted = ""
    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        formatted += f"{role}: {msg['content']}\n"
    return formatted + "Assistant: "

def append_to_history(history, role, content):
    history.append({"role": role, "content": content})
    return history
