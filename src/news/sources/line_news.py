import requests
from bs4 import BeautifulSoup

# filter for article element for LINE
def filter_line(element):
    if element.name == 'p' and not element.find('a'):
        return True
    return False

# extract news from LINE
def line_news(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title
    title = doc.find('h1').text.strip()

    # find article
    pieces = doc.find('article').find_all(filter_line)
    article = ''.join([piece.text for piece in pieces])

    # news
    news = "標題:\n"+title+"\n內文:\n"+article
    return news
