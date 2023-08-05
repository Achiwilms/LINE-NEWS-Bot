from src.news.sources.yahoo_news import yahoo_news
from src.news.sources.other_website import other_website

def extract_news(url):
    # Yahoo news
    if "news.yahoo.com" in url:
        return yahoo_news(url)
    # other website
    else:        
        return other_website(url)

