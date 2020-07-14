# pip install SpeechRecognition
# pip install pyaudio
# Microsoft Visual C + + 14.0 is required.
# Get it with "Microsoft Visual C++ Build Tools": https: // visualstudio.microsoft.com / downloads /

# Use "C:\Users\akumar6\Downloads>pip install PyAudio-0.2.11-cp38-cp38-win32.whl"

import speech_recognition as sr


def main():
    r=sr.Recognizer()
################################################## Using Microphone as the Input Audio Source ##################################################
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something...")
        audio=r.listen(source)
############################################ Using Audio file as the Input Audio source ########################################################
    # audio_file="Welcome.wav" #recorded_Audio_file1.wav"
    # with sr.AudioFile(audio_file) as source:
    #     audio = r.listen(source)
    #     print("Audio file loading ..Please wait ..")
######################################################################################################################################################
        try:
            print("You have said: \n" +r.recognize_google(audio))
        except Exception as e:
            print("Error: "+ str(e))


if __name__ == '__main__':
    main()


