import speech_recognition as sr
import webbrowser
from selenium import webdriver
import re

path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"  # Required if you use webbrowser
# global dest
def main():

    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please Say Something ..")
        audio=r.listen(source)

        print("Recognizing now.. Please wait ..")

        try:
            dest=r.recognize_google(audio)
            print("You have said: \n" + dest)
           # webbrowser.get(path).open_new_tab(dest)

        except Exception as e:
            print("Error: " + str(e))

        return dest

if __name__=='__main__':
    dest=main()
    match = re.search(r'\w+\.(com|in|org|edu|co)', dest)
    try:

        if (match.group()):
            print("Command Received .. Opening the URL..")
            driver = webdriver.Chrome()
            driver.get("http://www." + str(match.group()))
    except Exception:
        print("We did not find any matching website to open")


