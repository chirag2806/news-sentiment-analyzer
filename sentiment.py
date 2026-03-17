from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    score = sia.polarity_scores(text)

    if score['compound'] > 0.05:
        label = "Positive"
    elif score['compound'] < -0.05:
        label = "Negative"
    else:
        label = "Neutral"

    return label, score['compound']

def summarize_text(text):
    sentences = text.split(".")
    return ". ".join(sentences[:3]) + "."