from bs4 import BeautifulSoup
from utilites import dump, load
from nltk.tokenize import PunktSentenceTokenizer 
from nltk.tokenize import WordPunctTokenizer
from pymorphy2 import MorphAnalyzer

pst = PunktSentenceTokenizer()
wpt = WordPunctTokenizer()
ma = MorphAnalyzer()

def find_stop_words(text):
    rez = []
    for word in wpt.tokenize(text):
        tags = ma.parse(word)[0].tag
        if 'UNKN' in tags or \
           'LATN' in tags or \
           'PNCT' in tags or \
           'NUMB' in tags or \
           'ROMN' in tags:
            rez += [word]
    return rez

try:
    word_normal_form  = load('word_normal_form.json')
except FileNotFoundError:
    word_normal_form = {}

text = BeautifulSoup(open('lection.html').read(),'lxml').text

try:
    stop_words = set(load('stop_words.json'))
except FileNotFoundError:
    stop_words = find_stop_words(text)
    
def get_normal_form(word):
    try:
        nf = word_normal_form[word]
    except KeyError:
        nf = sorted(ma.parse(word), key=lambda x:x.score)[-1].normal_form
        word_normal_form.update({word:nf})
    return nf

def is_word(word):
    return not word in stop_words

sentences = {}
n = 0
for sentence in pst.tokenize(text):
    tokens = list(set([ get_normal_form(t) for t in wpt.tokenize(sentence) if is_word(t) ]))
    x = {
            n:{
                "tokens": tokens,
                "sentence": sentence
            }
    }
    sentences.update(x)
    n += 1
    
dump(sentences, 'intuit_sents.json')
dump(word_normal_form, 'word_normal_form.json')
dump(list(stop_words), 'stop_words.json')