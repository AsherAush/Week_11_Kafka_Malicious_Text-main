from textblob import TextBlob

# פונקצייה שמקבלת טקסט ומחזירה את הרגש שלו
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        return 'positive'
    elif polarity < -0.1:
        return 'negative'
    else:
        return 'neutral'
