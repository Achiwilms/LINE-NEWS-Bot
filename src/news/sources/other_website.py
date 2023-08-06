import requests
from bs4 import BeautifulSoup

# extract news from websites not listed
def other_website(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title (simply find h1)
    if doc.find('h1'):
        title = doc.find('h1').text
    else:
        title = ""

    # find article (simply join all paragraph)
    if doc.find('p'):
        pieces = doc.find_all('p')
        article = ''.join([piece.text.strip() for piece in pieces])
    else:
        article = ""

    # news
    news = "***\n標題:\n"+title+"\n內文:\n"+article+"\n***\n" 
    return news