from requests import get
from bs4 import BeautifulSoup as BS

WIKI_URL = "https://ru.wikipedia.org/wiki/%s"

def get_wiki_definition(word = "Дерево"):

    soup = BS(get(WIKI_URL % word).content, 'html.parser')
    
    try:
        y = soup.find('div','mw-content-ltr').find_all('p')
        myStr = ' '.join([ i.text for i in y ])
        return myStr
    except AttributeError as e:
        import sys
        print(word, e, file = sys.stderr)