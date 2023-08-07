from src.news.sources.yahoo_news import yahoo_news
from src.news.sources.line_short_url import line_short_url
from src.news.sources.line_news import line_news
from src.news.sources.other_website import other_website

def extract_news(url):
    # Yahoo news
    if (("news.yahoo.com" in url) or ("ynews" in url)):
        return yahoo_news(url)
    # LINE short url
    elif "liff.line" in url:
        return line_short_url(url)
    # LINE news
    elif "today.line" in url:
        return line_news(url)
    # other website
    else:        
        return other_website(url)

