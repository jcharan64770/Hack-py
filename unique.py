def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


list = [
    "https://music.youtube.com/watch?v=iznXe9d79jw&list=MLCT",
    "https://music.youtube.com/watch?v=SKm_GN2LaXU&list=MLCT",
    "https://music.youtube.com/watch?v=aDkEJ-DdA0w&list=MLCT",
    "https://music.youtube.com/watch?v=8m77vBdtnAs&list=MLCT",
    "https://music.youtube.com/watch?v=fNWK3HlD0-A&list=MLCT",
    "https://music.youtube.com/watch?v=Y9Qpya1AlXM&list=MLCT",
    "https://music.youtube.com/watch?v=xOxNrZBTuP4&list=MLCT",
    "https://music.youtube.com/watch?v=VPPKfQ3adc4&list=MLCT",
    "https://music.youtube.com/watch?v=4eHABt5SIgc&list=MLCT",
    "https://music.youtube.com/watch?v=VmkNFegq7VI&list=MLCT",
    "https://music.youtube.com/watch?v=o-yueRd-k0c&list=MLCT",
    "https://music.youtube.com/watch?v=R4hDcd9fzRk&list=MLCT",
    "https://music.youtube.com/watch?v=6PL39H2B7UQ&list=MLCT",
    "https://music.youtube.com/watch?v=xBqpEpMGZe8&list=MLCT",
]

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for excecuting tasks based on query
        if "what is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=100)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "who is" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=100)
            speak("According to wikipedia")
            print(results)
            speak(results)
