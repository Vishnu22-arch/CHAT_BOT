# utils/audio_utils.py
import os
import soundfile as sf
import librosa
from typing import Tuple
from config import SUPPORTED_AUDIO_TYPES, TEMP_AUDIO_PATH

def is_supported_audio_file(filename: str) -> bool:
    ext = os.path.splitext(filename)[1].lower()
    return ext in SUPPORTED_AUDIO_TYPES

def save_uploaded_file_to_wav(uploaded_file, target_path: str = TEMP_AUDIO_PATH) -> str:
    raw_path = target_path
    with open(raw_path, "wb") as f:
        f.write(uploaded_file.read())
    # normalize to 16k mono
    y, sr = librosa.load(raw_path, sr=16000, mono=True)
    sf.write(target_path, y, sr)
    return target_path

def load_audio_info(audio_path: str) -> Tuple[float, int]:
    y, sr = librosa.load(audio_path, sr=None)
    duration = len(y) / sr
    return duration, sr
