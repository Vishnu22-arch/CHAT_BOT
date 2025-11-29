# utils/prompt_engine.py

def build_chat_prompt(history, user_message):
    system_instruction = (
        "You are Nova, an intelligent assistant. Answer concisely and helpfully. "
        "Never output HTML or UI markup. Keep replies in plain text."
    )

    conversation = system_instruction + "\n\n"
    for turn in history:
        role = turn.get("role", "user")
        content = turn.get("content", "")
        if role == "user":
            conversation += f"User: {content}\n"
        else:
            conversation += f"Assistant: {content}\n"

    conversation += f"User: {user_message}\nAssistant:"
    return conversation
