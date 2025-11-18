import pyttsx3

def speak(text, confirmation=None):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for v in voices:
        if ('en_US' in v.id or 'en_GB' in v.id) and ('Samantha' in v.id or 'Victoria' in v.id or v.gender == 'VoiceGenderFemale'):
            engine.setProperty('voice', v.id)
            break
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 1.0)
    if confirmation:
        engine.say(confirmation)
    engine.say(text)
    engine.runAndWait()

