import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import os

USE_GTTS = True  

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)

    if USE_GTTS:
        filename = f"voice_{int(time.time())}.mp3"
        tts = gTTS(text=text, lang="en")
        tts.save(filename)
        playsound(filename)
        os.remove(filename)
    else:
        engine.stop()
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.3)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="en-in")
        print("You said:", command)
        return command.lower()
    except:
        speak("Sorry, I did not understand")
        return "none"

time.sleep(1)
speak("Hello, I am your voice assistant. I am ready.")

while True:
    command = listen()

    if command == "none":
        continue

    if "hello" in command:
        speak("Hello! Nice to meet you.")

    elif "time" in command or "timing" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "date" in command or "day" in command:
        today = datetime.datetime.now().strftime("%d %B %Y")
        speak(f"Today's date is {today}")

    elif "search" in command:
        speak("What should I search for?")
        query = listen()
        if query != "none":
            webbrowser.open(f"https://www.google.com/search?q={query}")
            speak(f"Searching {query}")

    elif "stop" in command or "exit" in command:
        speak("Goodbye. Have a nice day.")
        break

    else:
        speak("Sorry, I don't understand that yet.")
