# model/asr_model.py
from transformers import pipeline
from config import ASR_MODEL_NAME

_asr_pipeline = None

def get_asr_pipeline():
    global _asr_pipeline
    if _asr_pipeline is None:
        _asr_pipeline = pipeline("automatic-speech-recognition", model=ASR_MODEL_NAME)
    return _asr_pipeline

def transcribe_audio(audio_path: str) -> str:
    try:
        asr = get_asr_pipeline()
        result = asr(audio_path)
        # many pipelines return dict with 'text'
        if isinstance(result, dict) and "text" in result:
            return result["text"].strip()
        # fallback to string
        return str(result)
    except Exception as e:
        return "[ASR error: " + str(e) + "]"
