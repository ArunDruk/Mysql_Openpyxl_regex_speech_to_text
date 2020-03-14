# pip install gtts
# gtts : Google text to speech services

from gtts import gTTS
import os

fr=open("Text_speech_converter.txt")
Data=fr.read()

language='en'
audio=gTTS(text=Data,lang=language,slow=False)

audio.save("1.wav")
os.system("1.wav")