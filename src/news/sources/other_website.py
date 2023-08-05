import requests
from bs4 import BeautifulSoup

# extract news from websites not listed
def other_website(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title (simply find h1)
    title = doc.find('h1').text

    # find article (simply join all paragraph)
    pieces = doc.find_all('p')
    article = ''.join([piece.text.strip() for piece in pieces])

    # news
    news = "標題:\n"+title+"\n內文:\n"+article 
    return news