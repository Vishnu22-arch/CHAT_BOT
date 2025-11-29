# model/groq_model.py
# =====================================================================
# GROQ model wrapper — sanitizes history, enforces plain-text output
# =====================================================================

from groq import Groq
import os
import re

# Read API key from env var GROQ_API_KEY (set this before running)
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

def clean_html(raw):
    if not isinstance(raw, str):
        return raw
    return re.sub(r"<[^>]+>", "", raw).strip()

def sanitize_history(history):
    """Return a cleaned copy of history with only allowed roles."""
    allowed_roles = {"system", "user", "assistant"}
    sanitized = []
    for m in history:
        role = m.get("role", "user")
        if role not in allowed_roles:
            role = "user"
        sanitized.append({"role": role, "content": clean_html(m.get("content", ""))})
    return sanitized

def generate_groq_response(history):
    """
    history: list of dicts with keys 'role' and 'content'. Roles must be 'user'/'assistant'/'system'.
    Returns a plain-text reply string (HTML stripped).
    """

    clean_hist = sanitize_history(history)

    # system instruction forcing plain-text replies
    system_msg = {
        "role": "system",
        "content": (
            "You are Nova, a helpful assistant. Respond using ONLY plain text. "
            "Do not output HTML, CSS, or front-end markup. "
            "Do not wrap answers in <div>, <span>, or any tags. "
            "If asked to output code, return code blocks without additional HTML."
        )
    }

    # build messages list: system first, then sanitized history
    messages = [system_msg] + clean_hist

    # call the Groq chat API (client must be setup with valid API key)
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-maverick-17b-128e-instruct",
        messages=messages,
        temperature=0.7,
        max_completion_tokens=300,
        top_p=1,
        stream=False
    )

    reply = completion.choices[0].message.content.strip()
    return clean_html(reply)
