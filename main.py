import pyjokes
import pyttsx3
import speech_recognition
import requests
import datetime
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 150
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query






if __name__ == "__main__":
    while True:

        query = takeCommand().lower()
        if "wake up" in query:
            from greetMe import greetMe

            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Okay, Good Bye sir")
                    exit()
                elif "hello" in query:
                    speak("Hello sir, how are you?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("Perfect sir")
                elif "thank you" in query:
                    speak("you are welcome!")

                elif "play a game" in query:
                    from game import game_play

                    game_play()


                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    from keyboard import volumeup

                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown

                    speak("Turning volume down, sir")
                    volumedown()

                elif "open" in query:
                    from dictApp import openappweb

                    openappweb(query)
                elif "close" in query:
                    from dictApp import closeappweb

                    closeappweb(query)

                elif "google" in query:
                    from searchNow import searchGoogle

                    searchGoogle(query)
                elif "youtube" in query:
                    from searchNow import searchYoutube

                    searchYoutube(query)
                elif "wikipedia" in query:
                    from searchNow import searchWikipedia

                    searchWikipedia(query)

                elif "news" in query:
                    from NewsRead import latestnews

                    latestnews()


                elif "calculate" in query:
                    from Calculatenumbers import Calc

                    query = query.replace("calculate", "")
                    query = query.replace("veronica", "")
                    Calc(query)



                elif "temperature" in query:
                    endpoint="https://api.openweathermap.org/data/2.5/weather"
                    query_params={
                        'q':'Islamabad, PK',
                        'units': "imperial",
                        'lang':"en",
                        'mode':"json",
                        'appid': "980a47375d9ef16a1deab718b31ef779"

                    }
                    search = "temperature in islamabad"
                    response=requests.get(endpoint,params=query_params)
                    response=response.json();
                    speak("temperature is "+str(response['main']['temp'])+" degree farenheit")
                elif "weather" in query:
                    endpoint = "https://api.openweathermap.org/data/2.5/weather"
                    query_params = {
                        'q': 'Islamabad, PK',
                        'units': "imperial",
                        'lang': "en",
                        'mode': "json",
                        'appid': "980a47375d9ef16a1deab718b31ef779"

                    }
                    response = requests.get(endpoint, params=query_params)
                    response = response.json();
                    print(response)
                    speak("In Islamabad there are chances of  " + str(response['weather'][0]['description']))

                elif "joke" in query:
                    speak(pyjokes.get_joke())

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")




