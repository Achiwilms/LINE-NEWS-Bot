import requests
from bs4 import BeautifulSoup

# filter for article element for yahoo
def filter_yahoo(element):
    if element.name == 'p' and not element.find('br'):
        return True
    return False

# extract news from yahoo.com
def yahoo_news(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title
    doc_title = doc.find('div', class_='caas-title-wrapper')
    title = doc_title.find('h1').text.strip()

    # find article
    pieces = doc.find('div', class_='caas-body').find_all(filter_yahoo)
    article = ''.join([piece.text for piece in pieces])
    
    # news
    news = "標題:\n"+title+"\n內文:\n"+article
    return news