# model/text_model.py

from transformers import pipeline
from config import TEXT_MODEL_NAME, MAX_RESPONSE_TOKENS

_text_gen_pipeline = None


def get_text_generator():
    """
    Lazy-load and cache the text generation pipeline.
    """
    global _text_gen_pipeline
    if _text_gen_pipeline is None:
        _text_gen_pipeline = pipeline(
            task="text-generation",
            model=TEXT_MODEL_NAME
        )
    return _text_gen_pipeline


def generate_text(prompt: str, max_new_tokens: int = 60) -> str:
    generator = get_text_generator()
    outputs = generator(
        prompt,
        max_new_tokens=60,
        temperature=0.4,
        top_p=0.8,
        repetition_penalty=1.5,
        no_repeat_ngram_size=3,
        do_sample=True,
        truncation=True
    )

    text = outputs[0]["generated_text"]

    if text.startswith(prompt):
        text = text[len(prompt):]

    # Stop at first accidental role flip
    for stop_word in ["User:", "Assistant:"]:
        if stop_word in text:
            text = text.split(stop_word)[0]

    return text.strip()

