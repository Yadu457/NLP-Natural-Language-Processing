import speech_recognition as sr
from textblob import TextBlob
import pyttsx3

# initialize engine
engine = pyttsx3.init()

# initialize recognizer
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now...")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("You said:", text)

    # sentiment analysis
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive sentiment"
    elif polarity < 0:
        sentiment = "Negative sentiment"
    else:
        sentiment = "Neutral sentiment"

    print("Sentiment:", sentiment)
    engine.say(sentiment)
    engine.runAndWait()

except sr.UnknownValueError:
    print("Sorry, I could not understand the audio")
    engine.say("Sorry, I could not understand the audio")
    engine.runAndWait()

except sr.RequestError:
    print("Speech service error")
