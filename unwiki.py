#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 14:05:25 2019

@author: dan
"""
import re

def unwiki(keywords):
    for word in keywords:
        yield re.sub(r"[^a-z^а-я^-]+", "", word)
        
if __name__ == '__main__':
    print(list(unwiki(["лингви ́ стика"])))
    