import whisper
import os

# Load the small local Whisper model once
model = whisper.load_model("small")

def transcribe_audio(file_path):
    """
    Transcribes audio using OpenAI Whisper locally (no internet).
    Returns the text transcript.
    """
    if not os.path.exists(file_path):
        print(f"⚠️ Audio file not found: {file_path}")
        return None

    print(f"🎧 Transcribing locally: {file_path}")
    try:
        result = model.transcribe(file_path)
        text = result["text"].strip()
        print(f"🗣️ Muse heard: {text}")
        return text
    except Exception as e:
        print(f"❌ Local Whisper error: {e}")
        return None

if __name__ == "__main__":
    # quick test
    sample_audio = "assets/audio/user_input_test.wav"
    if os.path.exists(sample_audio):
        print(transcribe_audio(sample_audio))
    else:
        print("⚠️ No sample audio file found.")

