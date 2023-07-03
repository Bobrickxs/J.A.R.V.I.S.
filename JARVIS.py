import webbrowser

import speech_recognition as sr
import sys
import os
import pyttsx3
engine = pyttsx3.init()

import openai

from dotenv import load_dotenv as ld

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    ld(dotenv_path)

openai.api_key = os.getenv("api_key")

def handle_input(user_input):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}])
    return completion





def talk(words):
    print(words)
    engine.say(words)
    engine.runAndWait()
    #os.system("say " + words)


talk('Hi, can i help you?')

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Say')
        r.pause_threshold = 1
        #r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio,language='en-US').lower()
        print(task)
    except sr.UnknownValueError:
        talk('Я вас не зрозумів')
        task= command()


    return task


def make_something(task):
    if 'open site' in task:
        talk('Відкриваю')
        url = 'https://it-univer.thecabinet.io/profile/account_myorders/ '
        webbrowser.open(url)
    elif "ім'я" and "твоє" in task:
        talk("My name`s JARVIS")

    elif "стоп" in task:
        talk("Good buy")
        sys.exit()
    else:
        ai_response = handle_input(task).choices[0].message.content
        talk(ai_response)

while True:
    make_something(command())