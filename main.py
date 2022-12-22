# MyPcassistant
# importing required Libraries
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# Setting voices
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[1].id)

# Defining audio Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function for generating wish
def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir")
    elif hour>=12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("i am your assistant sir how may help you")

# This will take commands in the for of audio and convert it into string formate
def takeCommand():
    #it will take a command from user by microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listing...........")
        r.pause_threshold = 1
        audio = r.listen(source)
# Here is try block for catching the exception if any occurs in voice recognizing
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said :{query}\n")

    except Exception as e:

        print("Sorry will you please say again..")
        return "none"
    return query
# main function
if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        # here is logics for execution given commands

        if 'wikipedia' in query:
            speak("searching please wait....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia ")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening youtube...")
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            speak("opening facebook...")
            webbrowser.open("facebook.com")

        elif 'open gmail' in query:
            speak("opening youtube...")
            webbrowser.open("gmail.com")

        elif 'open google' in query:
            speak("opening google...")
            webbrowser.open("google.com")

        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("https://github.com/")

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"sir the time is{strTime} ")

        elif 'open vlc' in query:
            vlcPath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
            speak("opening vlc")
            os.startfile(vlcPath)

        elif 'open pycharm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2022.3\\bin\\pycharm64.exe"
            speak("opening pycharm..")
            os.startfile(pycharmPath)

        elif 'turn off buddy' in query:
            speak("turning off sir see you soon have fun")
            exit()

