import requests
from bs4 import BeautifulSoup

# extract news from news_lens
def news_lens(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title
    title = doc.find('h1').text.strip()

    # find article
    pieces = doc.find('article', itemprop='articleBody').find_all('p')
    article = ''.join([piece.text for piece in pieces])

    # news
    news = "標題:\n"+title+"\n內文:\n"+article
    return news



