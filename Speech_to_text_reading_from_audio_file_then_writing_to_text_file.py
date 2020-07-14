# pip install SpeechRecognition
# pip install pyaudio
# Microsoft Visual C + + 14.0 is required.
# Get it with "Microsoft Visual C++ Build Tools": https: // visualstudio.microsoft.com / downloads /

# Use "C:\Users\akumar6\Downloads>pip install PyAudio-0.2.11-cp38-cp38-win32.whl"

import speech_recognition as sr


def main():
    r=sr.Recognizer()

############################################ Using Audio file as the Input Audio source ########################################################
    audio_file="Welcome.wav" #recorded_Audio_file1.wav"
    with sr.AudioFile(audio_file) as source:
        audio = r.listen(source)
        print(type(audio))
        print(f"Audio file loading ..'{audio_file}'..")
######################################################################################################################################################
        try:
            print("You have said: \n" +r.recognize_google(audio)) #r.recognize_sphinx(audio))

        except Exception as e:
            print("Error: "+ str(e))

        output_file='Output_Speech_to_text.txt'
        print(f"\n\n We are writing the output to the text file: '{output_file}'..")
        Data=str(r.recognize_google(audio))
        L1=Data.split()
        word_limit=20

        with open(output_file, 'w') as fw:
            for i in range(0, len(L1), word_limit):
                s = " ".join(L1[i:i + word_limit])
                fw.write(s + '\n')

if __name__ == '__main__':
    main()
