#!/usr/bin/env python3
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:
    #print("Voice:")
    print(" - ID: %s" % voice.id, voice.name)
    #print(" - Name: %s" % voice.name)
    #print(" - Languages: %s" % voice.languages)
    #print(" - Gender: %s" % voice.gender)
    #print(" - Age: %s" % voice.age)#


def text_to_speech(text, output_file):
    speaker = pyttsx3.init()
    speaker.setProperty('voice', 'czech') 
    speaker.setProperty('rate', 150) # 200 defa.
    speaker.save_to_file(text, output_file)
    speaker.runAndWait()


text = "Toto je testovací text, který bude převeden na zvukový soubor."
output_file = "data/output_cz.mp3"

text_to_speech(text, output_file)