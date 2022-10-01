import speech_recognition
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour <= 12:
        speak("Good Morning")

    elif 12 <= hour <= 18:
        speak("Good Afternoon")

    else:
        speak("Good evening")

    speak("I am Jarvis! manthan, How may I help you?")

