#!/usr/bin/python3
import sys

from get_definition import get_definition
from get_keywords2 import get_keywords, filter_keywords
from stop_words import is_stop_word

tree = {}

def get_graph(word = "Дерево", n = 3):
    global tree

    count = 0
    word = word.lower()

    if n > 0:
        definition = get_definition(word)
        open('/tmp/rez.txt','a').write("=\n%s\n=\n" % definition)

        keywords = get_keywords(definition)
        
        keywords = filter_keywords(keywords)

        for word_i in keywords:
            if word_i != word and not is_stop_word(word_i):
                count += 1
                if get_graph(word_i, n - 1):
                    tree.update({(word, word_i):1})
    return count


if __name__ == '__main__':
    get_graph("Прикладная лингвистика", 2)
    print("digraph g {\n\trankdir=LR;")
    for definition, word in tree.keys():
        print("\t\"%s\" -> \"%s\"" % (definition, word))
    print("}")
	#graph = get_graph(definition = "дерево")
	# понятие -> понятие2
