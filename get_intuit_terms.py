from rutermextract import TermExtractor
from bs4 import BeautifulSoup
from utilites import dump
from get_intuit_sentences import get_normal_form

te = TermExtractor()

try:
    word_normal_form  = load('word_normal_form.json')
except FileNotFoundError:
    word_normal_form = {}
    
text = BeautifulSoup(open('lection.html').read(),'lxml').text
terms = te(text)
terms = [ ([ get_normal_form(x) for x in str(term).split() ],term.count) for term in terms if str(term).count(' ') > 1 ]
dump(terms, 'intuit_terms.json')