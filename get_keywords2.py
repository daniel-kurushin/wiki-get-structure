#!/usr/bin/python3
from rutermextract import TermExtractor
from pymystem3 import Mystem
ma = Mystem()

def get_keywords(text = ""):
    terms = TermExtractor()(text)
    try:
        max_count = terms[0].count
        for term in terms:
            if term.count >= max_count / 10:
                
                yield term.normalized 
    except IndexError as e:
        import sys
        print(text, e, file = sys.stderr)
        

def filter_keywords(keywords = ["россия", "бердяев", "информатика"], filter = set (["гео", "фам", "англ", "википедия", "такая страница", "такая статья"])):
	for keyword in keywords:
		params = []
		for a in ma.analyze(keyword):
			try:
				params += a['analysis'][0]['gr'].split(',')
			except (KeyError, IndexError):
				pass
		if not filter & set(params + [keyword]) and not len(keyword) < 3:
			yield keyword

if __name__ == '__main__':
	print(get_keywords("несогласованное использование табуляции несогласованное использование табуляции и пробелов в отступах несогласованное использование табуляции и пробелов в отступах"))
#	print(filter_keywords())
