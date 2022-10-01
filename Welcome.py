 elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open my website" in query:
            webbrowser.open("techfornerdz.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open whatsapp" in query:
            webbrowser.open("web.whatsapp.com")
        elif "play naruto music" in query:
            webbrowser.open(
                "https://music.youtube.com/watch?v=X4fIqbUjEEI&list=RDAMVMX4fIqbUjEEI"
            )
        elif "play hindi music" in query:
            webbrowser.open(
                "https://music.youtube.com/watch?v=NeXbmEnpSz0&list=RDAMVMNeXbmEnpSz0"
            )
        elif "play music" in query:
            x = random.randint(0, 13)
            webbrowser.open(list[x])

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir ji time is {strTime}")

        elif "open chrome" in query:
            filesPath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(filesPath)

        elif "who are you" in query:
            speak("I am JARVIS! your e-friend; Or you can say... your robo-friend.")

        elif "quit" in query:
            speak("Bye Bye manthan, have a nice day!")
