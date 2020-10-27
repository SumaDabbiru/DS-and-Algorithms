#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 17:25:15 2020

@author: SujithPatnaik
"""
import collections

def topKFrequent(words, k):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    candidates = count.keys()
    print(candidates)
    candidates= sorted(candidates, key = lambda w: (-count[w], w))

    print(candidates)
    return candidates[:k]

words = ["i", "love", "leetcode", "i", "love", "coding"]
k=2
print(topKFrequent(words, k))
