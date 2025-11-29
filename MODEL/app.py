# =====================================================================
# FINAL — CLEAN, ERROR-FREE, BUBBLE-FREE Streamlit Chat App
# =====================================================================

import streamlit as st
import time
import re
import uuid
import importlib

# Reload Groq model (avoid Streamlit caching)
import model.groq_model as groq_model_module
importlib.reload(groq_model_module)
from model.groq_model import generate_groq_response

# Optional mic
try:
    from audio_recorder_streamlit import audio_recorder
    MIC_AVAILABLE = True
except:
    MIC_AVAILABLE = False


# ================================
# UTIL — Remove HTML tags
# ================================
def clean_html(raw):
    if not isinstance(raw, str):
        return raw
    return re.sub(r"<[^>]+>", "", raw).strip()


# ================================
# PAGE CONFIG
# ================================
st.set_page_config(page_title="Nova AI", page_icon="🤖", layout="wide")


# ================================
# SESSION STATE INITIALIZATION
# ================================
if "history" not in st.session_state:
    st.session_state.history = []

if "processing" not in st.session_state:
    st.session_state.processing = False

if "chat_input" not in st.session_state:
    st.session_state.chat_input = ""

# IMPORTANT: flag to safely clear input
if "clear_input" not in st.session_state:
    st.session_state.clear_input = False


# ================================
# CLEAR INPUT BEFORE widget loads
# ================================
if st.session_state.clear_input:
    st.session_state.chat_input = ""
    st.session_state.clear_input = False


# ================================
# CSS (clean, no bubbles)
# ================================
st.markdown("""
<style>
body { background: #0f172a; color: #e5e5e5; }

/* Chat padding (space for input bar) */
.chat-area {
    padding-bottom: 200px;
}

/* Input bar fixed to bottom */
.input-wrapper {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    width: 900px;
    background: #1f2937;
    padding: 12px 18px;
    border-radius: 30px;
    display: flex;
    align-items: center;
    gap: 12px;
    box-shadow: 0 6px 30px rgba(0,0,0,0.35);
    border: 1px solid #334155;
}

/* Align user right */
.stChatMessage[data-testid="stChatMessageUser"] {
    text-align: right !important;
}

/* Align assistant left */
.stChatMessage[data-testid="stChatMessageAssistant"] {
    text-align: left !important;
}

.typing {
    font-style: italic;
    color: #94a3b8;
}
</style>
""", unsafe_allow_html=True)


# ================================
# DISPLAY CHAT
# ================================
st.markdown("<div class='chat-area'>", unsafe_allow_html=True)

for msg in st.session_state.history:
    st.chat_message(msg["role"]).write(msg["content"])

if st.session_state.processing:
    st.chat_message("assistant").write("⏳ Nova is typing...")

st.markdown("</div>", unsafe_allow_html=True)


# ================================
# INPUT BAR
# ================================
st.markdown("<div class='input-wrapper'>", unsafe_allow_html=True)

col_mic, col_text, col_send = st.columns([1, 8, 1])

# MIC
with col_mic:
    audio_bytes = None
    if MIC_AVAILABLE:
        recorded = audio_recorder("", icon_size="2x")
        if recorded:
            audio_bytes = recorded


# TEXT FIELD (stable key)
with col_text:
    user_text = st.text_input(
        "",
        placeholder="Message Nova...",
        key="chat_input",
        label_visibility="collapsed"
    )

# SEND BUTTON
with col_send:
    send_pressed = st.button("➤", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)


# ================================
# PROCESS USER INPUT
# ================================
user_message = None

# Voice message
if audio_bytes and not st.session_state.processing:
    user_message = "[voice message received]"

# Text message
if send_pressed and st.session_state.chat_input.strip() and not st.session_state.processing:
    user_message = clean_html(st.session_state.chat_input.strip())

    # SAFELY clear input on next rerun
    st.session_state.clear_input = True

    # Add user message
    st.session_state.history.append({
        "role": "user",
        "content": user_message
    })

    st.session_state.processing = True
    st.rerun()


# ================================
# MODEL RESPONSE
# ================================
if st.session_state.processing:

    # Clean history before sending
    cleaned_history = [
        {
            "role": msg["role"],
            "content": clean_html(msg["content"])
        }
        for msg in st.session_state.history
    ]

    # Get model reply
    bot_reply = generate_groq_response(cleaned_history)

    # HTML kill-switch
    bot_reply = clean_html(bot_reply).replace("<", "").replace(">", "")

    # Typing animation
    temp = st.empty()
    stream = ""
    for ch in bot_reply:
        stream += ch
        temp.chat_message("assistant").write(stream)
        time.sleep(0.01)
    temp.empty()

    # Save assistant reply
    st.session_state.history.append({
        "role": "assistant",
        "content": bot_reply
    })

    st.session_state.processing = False
    st.rerun()
