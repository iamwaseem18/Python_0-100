import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import pygame
import os
from openai import OpenAI
from gtts import gTTS


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "efa33978f4c34f0d80d5dd37812c2ffd"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()

# Load your MP3 file
    pygame.mixer.music.load("temp.mp3")

# Play the music
    pygame.mixer.music.play()

# Keep the program running until the music stops
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

os.remove('temp.mp3')

def aiprocess(command):
    client = OpenAI(api_key = "Enter your openapi key")
    
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant.Give short responses"},
        {"role": "user", "content": command}
    ]
)
    return completion.choices[0].message 

def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            #Parse the json response
            data = r.json()

            #Extract the articles
            articles = data.get('articles',[])

            #print the headlines 
            for article in articles:
                speak(article['title'])

        #Let openai handle the request

    else:
        output = aiprocess(c)
        speak(output)
        pass
    

if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        #Listen for the wake word Jarvis
        #Obtain audio from the microphone
        r = sr.Recognizer()

        print("Recognizning....")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() =="jarvis"):
                speak("Ya")
            
                #Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Activated...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processcommand(command)

        except Exception as e:
            print("Error; {0}".format(e))

