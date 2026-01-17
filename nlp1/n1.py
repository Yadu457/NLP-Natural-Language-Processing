import pyttsx3 #required import

#initialize engine
engine=pyttsx3.init()

#input text
text=input("Enter text in english:")

#speak text
engine.say(text)
engine.runAndWait()
