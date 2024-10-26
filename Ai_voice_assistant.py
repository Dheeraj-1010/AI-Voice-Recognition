import pyttsx3   #convert text to speech
import speech_recognition as sr
import webbrowser  #for web searching
import datetime   #for knowing current time
import pyjokes    #for random joke
import os
import time

def sptext():
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            try:
                print("Recognizing...")
                data = recognizer.recognize_google(audio)
                print(data)
                return data
            except sr.UnknownValueError:
                print("Not Understand")
        
#text to speech
def speechtx(x):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  #0 for male or 1 for female
    rate = engine.getProperty('rate')
    engine.setProperty('rate',100)   #voice speed
    engine.say(x)
    engine.runAndWait()

if __name__ == '__main__':
    
    if "hello virtual assistant" in sptext().lower():
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "I don't have any name, I am Dheeraj personal Assistant."
                speechtx(name)
            elif "old are you" in data1:
                age = "I am 19 years old"
                speechtx(age)
            elif "time now" in data1:
                curr_time = datetime.datetime.now().strftime("%I%M%p")
                speechtx(curr_time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "spotify" in data1:
                webbrowser.open("https://open.spotify.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en",category="neutral")
                print(joke_1)
                speechtx(joke_1)
            elif "play song" in data1:
                add = "C:\\Users\\Dheeraj\\Desktop\\Song"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[1])) 

            elif "exit" in data1:
                speechtx("Thank you")
                break
            time.sleep(3)
    else:
       print("Thanks")
        