

# NEED TO INSTALL ALL THE MODULES.
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
from translate import Translator
import python_weather
import asyncio




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices) # this will select voices and speak function
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# A wish me function  to be wished every time we run this code
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon")
 
    else:
        speak("good evening")

    speak("Hello. How can i help you")
# # MAin command to recognize, use microphone is a function of speech_recognition
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning...")
        r.pause_threshold = 1
        audio = r.listen(source)
# # this is for recognize voice,  if the words said,  matches with any of the statements, it will answer
    try:
        print("Recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:  {query}\n")
    # if it cant recognise it will say this
    except Exception as e:
        # print(e)

        speak("sorry can't recognise, or try connecting to network")
        return "nothing"
    return query
# this is for calling or running programs
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

# #  This code is just for giving commands and opening apps or webpages
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
            


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            opening = ("opening")
            speak(f"{opening}youtube")

        elif 'open google' in query:
            webbrowser.open("google.com")
            opening = ("opening")
            speak(f"{opening}google")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")    
            opening = ("opening")
            speak(f"{opening}facebook")

        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
            opening = ("opening")
            speak(f"{opening}instagram")   

        elif 'play music' in query:
            webbrowser.open("spotify.com")
            spoti = ("playing music on spotify")
            speak(f"{spoti}") 

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H: %H: %S")        
            speak(f"sir, the time is {strTime}")   

        elif 'what is your name' in query:
            name = ("kelly")
            speak(f"my name is{name}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\$yourdrivename$\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            opening = ("opening")
            speak(f"{opening}")

        elif 'what is' in query:
            webbrowser.open('google.com')
            opening = ("opening")
            speak(f"{opening}google you can search on it")

        elif 'what can you do' in query:
            say = ('''You can try saying, Open Youtube, Open Google, open facebook, open instagram, play music 
            , what is the time , open code, what is''')
            print(say)
            speak(f"{say}")
                

        elif 'open chrome' in query:
            codePAth = "C:\\Users\\$yourdrivename$\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(codePAth)
            opening = ("opening")
            speak(f"{opening}chrome")

        elif 'open amazon' in query:
            webbrowser.open('amazon.com')
            opening = ("opening")
            speak(f"{opening}amazon")    

        elif 'open flipkart' in query:
            webbrowser.open('flipkart.com')
            opening = ("opening")
            speak(f"{opening}flipkart")
# Chat bot TALKING function
        elif 'hello' in query:
            hello = ("hello sir what's going on")
            speak(f"{hello}")    

        elif 'hay' in query:
            hey = ("hey sir i think you are in a good mood")
            speak(f"{hey}")

        elif 'yes kelly' in query:
            yes = ("ohh good sir")
            speak(f"{yes}")

        elif 'iam fine' in query:
            ok = ("nice you should always be fine") 
            speak(f"{ok}")

        elif 'who is your father' in query:
            father = ("$your name$")
            speak(f"father")

        elif 'who is your developer' in query: 
            developer = ("TANISH")
            speak(f"{developer}")   

            # diciplinary code 
        elif "so kelly what's going on" in query:
            h = ("Nothing! I'm just learning nw things")
            speak(f"{h}")

        elif "ok kelly" in query:
            what = ("Tell me SIR! how can i help you" ) 
            speak(f"{what}")   

        # full bot
        elif "hi" in query:
            ab = ("Hi there! how can i help you")
            speak(f"{ab}")

        elif "how are you" in query:
            ac = ("Iam fine , i wish you'll always fine")
            speak(f"{ac}")

        elif "what are you doing" in query:
            ad = ("Just learning new things, you should also learn new things ")
            speak(f"{ad}")

        elif "thank you" in query:
            ae = ("hope you liked talking to me")
            speak(f"{ae}")

        elif "translate" in query:

            inp = str(input("enter first language : " ))
            inp2 = str(input("enter secon language : "))
            inp3 = str(input("enter text:  "))

            translator = Translator(from_lang = inp, to_lang = inp2)
            result = translator.translate(inp3)
            print(result)
            aaaa = (result)
            speak(f"{aaaa}")
        
        
        elif "Weather" or "weather" in query:
            place = input("PLace:  ")
            async def getweather():
                # declare the client. format defaults to metric system (celcius, km/h, etc.)
                client = python_weather.Client(format=python_weather.IMPERIAL)

                # fetch a weather forecast from a city
                weather = await client.find(place)

                # returns the current day's forecast temperature (int)
                # print(weather.current.temperature)
                pl = weather.current.temperature
                speak(f"weather conditions of {place} is {pl}")

                # get the weather forecast for a few days
                for forecast in weather.forecasts:
                    print(str(forecast.date), forecast.sky_text, forecast.temperature)

                # close the wrapper once done
                await client.close()

            if __name__ == "__main__":
                loop = asyncio.get_event_loop()
                loop.run_until_complete(getweather())
        

                


