from rutermextract import TermExtractor
from bs4 import BeautifulSoup
from utilites import dump

te = TermExtractor()

text = BeautifulSoup(open('lection.html').read(),'lxml').text
terms = te(text)
terms = [ (str(term).split(),term.count) for term in terms if str(term).count(' ') > 1 ]
dump(terms, 'intuit_terms.json')