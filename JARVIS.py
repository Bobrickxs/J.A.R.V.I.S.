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