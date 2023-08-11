import requests
from bs4 import BeautifulSoup

# filter for article element for ettoday
def filter_ettoday(element):
    if element.name == 'p' and not element.find('strong'):
        return True
    return False

# extract news from ETtoday
def ettoday_news(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title
    title = doc.find('h1').text.strip()

    # find article
    pieces = doc.find('div', class_='story').find_all(filter_ettoday)
    article = ''.join([piece.text for piece in pieces])

    # news
    news = "標題:\n"+title+"\n內文:\n"+article
    return news