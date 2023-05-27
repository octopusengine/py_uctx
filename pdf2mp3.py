#!/usr/bin/env python3
import pyttsx3, PyPDF2

pdf_file = "data/test.pdf"
pdfreader = PyPDF2.PdfReader(open(pdf_file, "rb"))


def text_to_speech(text, output_file):
    speaker = pyttsx3.init()
    speaker.setProperty('rate', 150) # 200 defa.
    #speaker.setProperty('voice', 'english+f1')  # intonation
    speaker.setProperty('voice', 'english-uk') 
    speaker.save_to_file(text, output_file)
    speaker.runAndWait()


text = pdfreader.pages[0].extract_text()
clean_text = text.strip().replace("\n"," ")
print(clean_text)

text_to_speech(clean_text, "data/test.mp3")
