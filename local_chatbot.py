from llm_connector import stream_response
from chat_manager import format_chat_history, append_to_history

def chat_with_mistral():
    print("LLMChat-Local_V0.1")
    print("Type your message below. Use 'reset' to clear history or 'exit' to quit.\n")

    chat_history = []

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Exiting chat.")
            break
        elif user_input.lower() == 'reset':
            chat_history = []
            print("Chat history cleared.\n")
            continue

        append_to_history(chat_history, "user", user_input)
        prompt = format_chat_history(chat_history)

        print("Mistral:", end=" ", flush=True)
        full_response = ""
        for chunk in stream_response(prompt):
            print(chunk, end="", flush=True)
            full_response += chunk

        print("\n")
        append_to_history(chat_history, "assistant", full_response)

if __name__ == "__main__":
    chat_with_mistral()
