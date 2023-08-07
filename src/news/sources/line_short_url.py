import requests
from bs4 import BeautifulSoup
from src.news.sources.line_news import line_news

# extract news from short url of LINE news 
def line_short_url(short_url):
    hotpage = requests.get(short_url)
    short_doc = BeautifulSoup(hotpage.text, 'html.parser')
    url = short_doc.a['href']
    return line_news(url)