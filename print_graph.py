#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:19:56 2019

@author: dan
"""
def print_graph(tree):
    print("digraph g {\n\trankdir=LR;")
    for word_i, word_j in tree.keys():
        w = tree[(word_i, word_j)]
        print("\t\"%s\" -> \"%s\" [penwidth=\"%s\"]" % (word_i, word_j, w))
    print("}")
