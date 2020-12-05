# pip install pyttsx3

import pyttsx3

sayMyNameBitch = input("Enter text that you would like me to say !?\n")

engine = pyttsx3.init()
engine.say(sayMyNameBitch)
engine.runAndWait()

