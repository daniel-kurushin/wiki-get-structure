from utilites import dump, load
from bs4 import BeautifulSoup
import numpy as np

sentences = load('intuit_sents.json')
terms = load('intuit_terms.json')

try:
    text = load('tet.json')
except FileNotFoundError:    
    candidates = []
    for tokens_a in ( set(x[0]) for x in terms ):
        for tokens_b, n in ( (set(sentences[x]['tokens']), x) for x in sentences):
            if tokens_a & tokens_b: 
                candidates += [(int(n), len(tokens_a & tokens_b) / len(tokens_b), tokens_a & tokens_b)]
                
    candidates = sorted(candidates, key=lambda x: x[1], reverse=1)
    
    text = open('text.csv','w')
    used = []
    tokens = candidates[0][2]
    for pos, q, tags in candidates:
        if q > 0:
            i = pos
            s = sentences[str(i)]
            if i not in used:
                text.write("%s ^ %s ^ %s\n" % (s['sentence'], i, q))
                used += [i]
    
    text.close()
    text = sorted(text, key=lambda x: x[1])
    dump(text, 'text.json')
    
out = BeautifulSoup("<body/>","lxml")
p = out.new_tag('p')
new = 1
for sentence, n in text:
    try:
        p.string += sentence
    except TypeError:
        p.string = sentence
    if np.random.choice(10) > 8:
        out.body.insert(len(out('p')),p)
        p = out.new_tag('p')

out.body.insert(len(out('p')),p)
open('/tmp/out.html', 'w').write(out.prettify())