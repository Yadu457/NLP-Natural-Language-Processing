import pyttsx3
from textblob import TextBlob

# initialize engine
engine = pyttsx3.init()

# input text
text = input("Enter text in English: ")

# sentiment analysis
analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

# determine sentiment
if polarity > 0:
    sentiment = "Positive sentiment"
elif polarity < 0:
    sentiment = "Negative sentiment"
else:
    sentiment = "Neutral sentiment"

# output
print("Sentiment:", sentiment)

# speak sentiment
engine.say(sentiment)
engine.runAndWait()
