import os
from dotenv import load_dotenv

load_dotenv()

NEWS_SOURCES = {
    'bbc': {
        'url': 'https://www.bbc.com/news',
        'rss_url': 'http://feeds.bbc.co.uk/news/rss.xml',
        'enabled': True
    },
    'cnn': {
        'url': 'https://www.cnn.com',
        'rss_url': 'http://rss.cnn.com/rss2.0/cnn_topstories.rss',
        'enabled': True
    },
    'guardian': {
        'url': 'https://www.theguardian.com/international',
        'rss_url': 'https://www.theguardian.com/world/rss',
        'enabled': True
    },
    'techcrunch': {
        'url': 'https://techcrunch.com',
        'rss_url': 'http://feeds.techcrunch.com/TechCrunch/',
        'enabled': True
    }
}

SENTIMENT_MODELS = {
    'vader': {
        'name': 'vader',
        'enabled': True
    },
    'transformers': {
        'model_name': 'distilbert-base-uncased-finetuned-sst-2-english',
        'enabled': True
    }
}

DATABASE_PATH = 'news_sentiment.db'
REQUEST_TIMEOUT = 10
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')