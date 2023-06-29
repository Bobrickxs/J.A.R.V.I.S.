import webbrowser

import speech_recognition as sr
import sys
import os
import pyttsx3


engine = pyttsx3.init()



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

while True:
    make_something(command())