import sounddevice as sd
import numpy as np
import webrtcvad
from scipy.io.wavfile import write
import os, time

def record_audio(fs=16000, max_duration=60, silence_limit=3):
    vad = webrtcvad.Vad(2)  # 0 = very sensitive, 3 = least
    frame_duration_ms = 30
    frame_length = int(fs * frame_duration_ms / 1000)
    audio_data = []
    silent_frames = 0

    print("🎤 Muse is listening! Speak freely, stop talking to let Muse reply.")
    stream = sd.InputStream(samplerate=fs, channels=1, dtype='int16')
    with stream:
        for i in range(int(max_duration * 1000 / frame_duration_ms)):
            frame, _ = stream.read(frame_length)
            frame_data = frame.tobytes()
            is_speech = vad.is_speech(frame_data, fs)
            audio_data.append(frame)
            if not is_speech:
                silent_frames += 1
            else:
                silent_frames = 0
            if silent_frames * frame_duration_ms > silence_limit * 1000:
                print("🛑 Detected silence. Stopping recording...")
                break

    audio_data = np.concatenate(audio_data, axis=0)
    os.makedirs("assets/audio", exist_ok=True)
    filename = f"assets/audio/user_input_{int(time.time())}.wav"
    write(filename, fs, audio_data)
    print(f"✅ Audio recorded: {filename}")
    return filename

if __name__ == "__main__":
    record_audio()

