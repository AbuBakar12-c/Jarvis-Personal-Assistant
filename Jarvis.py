import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import wikipedia
import webbrowser
from requests import get
import sys
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# text to speech and print
def speak(audio):
    print(f"Jarvis: {audio}")
    engine.say(audio)
    engine.runAndWait()

# Speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 10
        try:
            audio = r.listen(source, timeout=1, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("Listening timed out, please try again.")
            return "none"

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        speak("Say that again please...")
        return 'none'
    return query

# To Wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak('Good morning')
    elif hour >= 12 and hour < 18:
        speak('Good afternoon')
    else:
        speak("Good evening")
    speak('I am Jarvis sir. Please tell me how can I help you')

# For global access to the camera object
cap = None

if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()

        # --- NOTEPAD ---
        if "open notepad" in query:
            os.startfile("C:\\Windows\\system32\\notepad.exe")

        elif "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
            speak("Notepad closed successfully")

        # --- CAMERA ---
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            speak("Camera opened. Press Enter key to close.")
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(1) == 10:  # Enter key
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "close camera" in query:
            if cap and cap.isOpened():
                cap.release()
                cv2.destroyAllWindows()
                speak("Camera closed successfully")
            else:
                speak("Camera is not open")

        # --- SONG / YOUTUBE ---
        elif "play song" in query or "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com/")

        elif "close youtube" in query:
            os.system("taskkill /f /im chrome.exe")  # This will close Chrome completely
            speak("YouTube closed (browser closed)")

        # --- IP ADDRESS ---
        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"Your IP Address is {ip}")

        # --- WIKIPEDIA ---
        elif "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        # --- GITHUB ---
        elif "open github" in query:
            webbrowser.open("https://github.com/AbuBakar12-c")
        elif "close github" in query:
            os.system("taskkill /f /im chrome.exe")
            speak("GitHub closed")

        # --- CHATGPT ---
        elif "open chatgpt" in query:
            webbrowser.open("https://chatgpt.com/")
        elif "close chatgpt" in query:
            os.system("taskkill /f /im chrome.exe")
            speak("ChatGPT closed")

        # --- GMAIL ---
        elif "open gmail" in query:
            webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        elif "close gmail" in query:
            os.system("taskkill /f /im chrome.exe")
            speak("Gmail closed")

        # --- GOOGLE SEARCH ---
        elif "open google" in query:
            speak("Sir, what should I search on Google?")
            cm = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={cm}")
        elif "close google" in query:
            os.system("taskkill /f /im chrome.exe")
            speak("Google closed")

        # --- EXIT ---
        elif "no thanks" in query:
            speak("Thanks for using me sir, have a good day")
            sys.exit()

        # Continue asking
        speak("Sir, do you have any other work?")
