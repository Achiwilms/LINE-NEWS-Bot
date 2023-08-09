import requests
from bs4 import BeautifulSoup

# find irrelevent elements in Now news
def filter_nownews(element):
    if element.name == ('h2') or element.name == ('div'):
        return True
    return False

def now_news(url):
    hotpage = requests.get(url)
    doc = BeautifulSoup(hotpage.text, 'html.parser')

    # find title
    title = doc.find('h1', class_='article-title').text.strip()

    # find all irrelevent elements and extract them
    irre_elements = doc.find('article').find_all(filter_nownews)
    for irre_element in irre_elements:
        irre_element.extract()

    # find article
    article = doc.find('article').get_text(strip=True) 

    # news
    news = "標題:\n"+title+"\n內文:\n"+article
    return news