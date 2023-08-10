import requests
from bs4 import BeautifulSoup

# extract news from websites not listed (this works for most sites)
def other_website(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title (simply find h1)
    if doc.find('h1'):
        title = doc.find('h1').text.strip()
    else:
        raise Exception("找不到報導")

    # find article (simply join all paragraph)
    if doc.find('p'):
        pieces = doc.find_all('p')
        article = ''.join([piece.text.strip() for piece in pieces])
    else:
        raise Exception("找不到報導")

    # news
    news = "標題:\n"+title+"\n內文:\n"+article 
    return news