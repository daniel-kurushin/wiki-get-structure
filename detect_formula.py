#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:38:13 2019

@author: dan
"""

def is_formula(token):
    tags = {''}
    for var in token:
        tags |= var.tag.grammemes
    if {'LATN', 'UNKN'} & tags:
        chars = set(token[0].word)
        return chars
    else:
        return 0

if __name__ == '__main__':
    from pymorphy2 import MorphAnalyzer
    mo = MorphAnalyzer()
    for x in ['1/r²', '2*2=4', '\frac{2,2}', 'help', 'what is love', 'лингви́стика']:
        print(x, is_formula(mo.parse(x)))