# pip install gtts
# gtts : Google text to speech services

from gtts import gTTS
import os

########### To read text file and convert into speech ########################
fr=open("Text_speech_converter.txt")
Data=fr.read()

###################### To get the input from the user and convert to Speech
# Data=input("Enter your text pls: ")

language='en'
audio=gTTS(text=Data,lang=language,slow=False)

audio.save("1.wav")
os.system("1.wav")