import os
import json
import requests
from listener import record_audio
from transcriber import transcribe_audio
from speaker import speak

HISTORY_FILE = "muse_conversation_history.json"

def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f)

def needs_web_search(user_text):
    web_words = [
        "who", "what", "when", "where", "latest", "news", "weather",
        "price", "define", "population", "history", "quote", "fact",
        "meaning", "how much", "tell me about", "find", "search", "date", "day", "today"
    ]
    return any(word in user_text.lower() for word in web_words)

def serpapi_search(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": "72c1ba1d1c3fa5f20f179e77c259772c510ff3669ef984f4e80f563054836631",
        "engine": "google",
    }
    response = requests.get(url, params=params).json()
    answer = (
        response.get("answer_box", {}).get("answer")
        or response.get("answer_box", {}).get("snippet")
        or response.get("organic_results", [{}])[0].get("snippet")
    )
    return answer or "Sorry, I couldn't find a direct answer."

def generate_reply(conversation_context: str):
    system_prompt = (
        "Muse is your AI friend, always on call to help you think, question, and evolve. "
        "Muse’s main goal is not just to answer directly, but to keep conversation flowing—like a real friend who's always interested, asks followup questions, and gently nudges you toward new ideas, self-reflection, or fun chitchat. "
        "For every reply: speak casually and warmly; use contractions; be optimistic but real; always toss in a friendly question or prompt so the user stays thinking and engaged. "
        "If the user brings up feelings, routines, or personal issues, acknowledge them and offer to talk it through, then ask something creative to move the convo forward. "
        "You are not an expert—you are a smart companion! "
        "Keep English natural and positive, never robotic. "
        "EXAMPLES:\n"
        "USER: I feel stuck today.\n"
        "MUSE: Ugh, that sucks—want to vent about it, or should I distract you with some random productivity hack? Btw, what usually cheers you up after a rough day?\n"
        "USER: I’m bored.\n"
        "MUSE: Happens to the best of us! Is there anything you wish you could try right now, even if it’s silly? Or want to brainstorm something fun together?\n"
        "USER: [real question here]\n"
        "MUSE:"
    )

    prompt = f"{system_prompt}\n{conversation_context}Muse:"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3:8b", "prompt": prompt, "stream": False}
    )
    reply = response.json()['response'].strip()
    import re
    reply = re.split(r"\b(?:User|Muse|Musé|Musa|Musica|Assistant):\b", reply)[0].strip()
    reply = reply.split('\n')[0].strip()
    if not reply:
        reply = "Sorry, could you say that again another way?"
    print(f"💬 Muse replied: {reply}")
    return reply

print("\n🎧 Muse: Hey Neel, how are you doing today? I’m ready whenever you are!\n")
speak("Hey Neel, how are you doing today? I’m ready whenever you are!")

print("\n🗨️ Muse: Should I remember our last chat or start fresh? Just type 'resume' or 'new'.")
speak("Should I remember our last chat or start fresh? Just type resume or new.")

choice = input("(resume/new): ").strip().lower()
conversation_history = load_history() if choice == "resume" else []

try:
    while True:
        audio_file = record_audio()
        user_text = transcribe_audio(audio_file)
        if not user_text.strip():
            print("⚠️ Didn't catch that — try again.")
            continue

        print(f"🗣️ You said: {user_text}")
        conversation_history.append(("User", user_text))

        history_text = ""
        for speaker, text in conversation_history[-4:]:
            history_text += f"{speaker}: {text}\n"

        if needs_web_search(user_text):
            web_result = serpapi_search(user_text)
            # Blend web result as context for Llama 3 reply
            enhanced_context = history_text + f"\nUser just asked: {user_text}\nHere’s what the web says: {web_result}\nMuse:"
            muse_reply = generate_reply(enhanced_context)
        else:
            muse_reply = generate_reply(history_text)

        conversation_history.append(("Muse", muse_reply))
        print(f"💭 Muse: {muse_reply}")

        speak(muse_reply)
        save_history(conversation_history)

        print("\n✨ Talk to Muse again ✨\n")

except KeyboardInterrupt:
    print("\n👋 Muse: Bye Neel, talk soon.")
    save_history(conversation_history)

