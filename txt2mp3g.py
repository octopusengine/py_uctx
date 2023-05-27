#!/usr/bin/env python3
#  gTTS (Google Text-to-Speech) 
#  online / cloud :(

from gtts import gTTS

__version__ = "0.2.0" # 2023/02

input_file = "data/nostr1.txt"
output_file = "data/output_nostr1_g.mp3"

#text = "Toto je testovací text, který bude převeden na zvukový soubor."
with open(input_file, "r", encoding="utf-8") as file:
    text = file.read().replace("\n", " ")

print(text)

tts = gTTS(text,lang='cs',tld='com',slow=False) #-
#tts = gTTS(text,lang='cs',slow=True) #2 fakt pomale
tts.save(output_file)
