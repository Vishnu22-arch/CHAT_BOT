# inference.py
import os, sys
from model.asr_model import transcribe_audio
from model.text_model import generate_text
from utils.prompt_engine import build_chat_prompt
from utils.audio_utils import load_audio_info

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

def process_audio_file(audio_path: str) -> dict:
    transcription = transcribe_audio(audio_path)
    prompt = build_chat_prompt([], transcription)
    response = generate_text(prompt)
    duration, sr = load_audio_info(audio_path)
    return {
        "audio_path": audio_path,
        "sample_rate": sr,
        "duration_sec": duration,
        "transcription": transcription,
        "prompt": prompt,
        "response": response,
    }

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--audio", "-a", required=True)
    args = parser.parse_args()
    result = process_audio_file(args.audio)
    print(result)
