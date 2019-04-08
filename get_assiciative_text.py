#!/usr/bin/python3
import sys

from get_definition import get_definition
from get_keywords2 import get_keywords, filter_keywords
from stop_words import is_stop_word

tree = {}

def get_graph(word = "Дерево", n = 0):
    global tree

    word = word.lower()
    if n < 2:
        definition = get_definition(word)
        open('/tmp/rez.txt','a').write("=\n%s\n=\n" % definition)

        keywords = get_keywords(definition)
        
        print(keywords, definition, file = sys.stderr)

        keywords = filter_keywords(keywords)

        for word_i in keywords:
            if word_i != word and not is_stop_word(word_i):
                if get_graph(word_i, n+1):
                    tree.update({(definition, word_i):1})


if __name__ == '__main__':
    get_graph("Прикладная лингвистика", 0)
    print("digraph g {\n\trankdir=LR;")
    for definition, word in tree.keys():
        print("\t\"%s\" -> \"%s\"" % (definition, word))
    print("}")
	#graph = get_graph(definition = "дерево")
	# понятие -> понятие2
