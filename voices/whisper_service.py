from .whisper_client import get_whisper_model

def transcribe_audio_file(path):
    model = get_whisper_model()

    result = model.transcribe(
        path,
        language="ja",
        fp16=False,
    )
    text = (result.get("text") or "").strip()
    return text