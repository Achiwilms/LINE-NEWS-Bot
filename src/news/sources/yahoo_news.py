import requests
from bs4 import BeautifulSoup

# filter for article element
def filter_yahoo_paragraph(element):
    if element.name == 'p' and not element.find('br'):
        return True
    return False

# extract new from yahoo.com
def yahoo_news(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title
    doc_title = doc.find('div', class_='caas-title-wrapper')
    title = doc_title.find('h1').text

    # find article
    doc_art = doc.find('div', class_='caas-body')
    pieces = doc_art.find_all(filter_yahoo_paragraph)
    article = ''.join([piece.text for piece in pieces])
    
    # news
    news = "標題:\n"+title+"\n內文:\n"+article 
    return news