import os.path

import pyttsx3
import speech_recognition
import sys
import winsound
r=speech_recognition.Recognizer()
dir = os.path.dirname(os.path.abspath(sys.argv[0]))
def Listen():
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2,duration=1)
        SpeakText("say something")
        audio2 = r.listen(source2)
        try:
            MyText = r.recognize_google(audio2)
        except:
            SpeakText("didnt recognize voise")
            SpeakText("try again")
            Listen()
        MyText = MyText.lower()
    print(MyText)
    SpeakText(MyText)
    if MyText == "play song" or "music" or "play music" or "playmusic" or "song":
        SpeakText("Playing Song The Town by ethismos")
        winsound.PlaySound(dir +'/The Town.wav',winsound.SND_FILENAME)
def SpeakText(command):
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate-80)
    engine.say(command)
    engine.runAndWait()
Listen()
