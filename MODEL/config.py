# config.py
# configuration constants

ASR_MODEL_NAME = "openai/whisper-small"   # if using HuggingFace pipelines
TEXT_MODEL_NAME = "distilgpt2"
MAX_RESPONSE_TOKENS = 300
SUPPORTED_AUDIO_TYPES = [".wav", ".mp3", ".flac", ".ogg", ".m4a"]
TEMP_AUDIO_PATH = "temp_audio_input.wav"
