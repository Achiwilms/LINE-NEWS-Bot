from src.news.sources.yahoo_news import yahoo_news
from src.news.sources.line_short_url import line_short_url
from src.news.sources.line_news import line_news
from src.news.sources.now_news import now_news
from src.news.sources.ettoday_news import ettoday_news
from src.news.sources.news_lens import news_lens
from src.news.sources.other_website import other_website

def extract_news(url):
    # Yahoo news
    if (("yahoo.com" in url) or ("ynews" in url)):
        return yahoo_news(url)
    
    # LINE short url
    elif "liff.line" in url:
        return line_short_url(url)
    
    # LINE news
    elif "today.line" in url:
        return line_news(url)
    
    # Now news
    elif "nownews.com" in url:
        return now_news(url)
    
    # Ettoday news (not include forum)
    elif (("ettoday.net" in url) and not("forum.ettoday" in url)):
        return ettoday_news(url)
    
    # News Lens
    elif "thenewslens.com" in url:
        return news_lens(url)
    
    # other website
    else:        
        return other_website(url)

