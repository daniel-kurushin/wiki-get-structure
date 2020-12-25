#!/usr/bin/python3
import sys
import json

from get_definition import get_definition
from get_keywords2 import get_keywords, filter_keywords
from stop_words import is_stop_word
from tree import Tree
from unwiki import unwiki 
from print_graph import print_graph

tree = Tree()

def get_graph(word = "Дерево", n = 3):
    count = 0
    word = word.lower()

    if n > 0:
        definition = get_definition(word)
        open('/tmp/rez.txt','a').write("=\n%s\n=\n" % definition)
        for word_i in unwiki(filter_keywords(get_keywords(definition))):
            if word_i != word and not is_stop_word(word_i):
                count += 1
                if get_graph(word_i, n - 1):
                    try:
                        tree[(word, word_i)] += 1
                    except KeyError:
                        tree.update({(word, word_i):1})
    return count


if __name__ == '__main__':
    get_graph("Прикладная лингвистика", 2)
    print_graph(tree)
    print(json.dumps(tree))
	#graph = get_graph(definition = "дерево")
	# понятие -> понятие2
