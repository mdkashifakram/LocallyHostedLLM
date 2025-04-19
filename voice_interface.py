# voice_interface.py
#curently not being used.
'''
import speech_recognition as sr
import pyttsx3


recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

def listen_to_user():
    with sr.Microphone() as source:
        print("🎙️ Listening... (speak now)")
        audio = recognizer.listen(source)
        try:
            user_text = recognizer.recognize_google(audio)
            print(f"🗣️ You said: {user_text}")
            return user_text
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
            return ""
        except sr.RequestError as e:
            print(f"⚠️ STT service error: {e}")
            return ""

def speak_response(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

'''
