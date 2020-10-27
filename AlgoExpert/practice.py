#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:32:37 2020

@author: SujithPatnaik
"""

def mostCommonWord(paragraph,banned):

    normalized_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

    words = normalized_str.split()

    word_count = {}
    banned_words = set(banned)


    for word in words:
        if word not in banned_words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    
    sortedWords = sorted(word_count.items(),key=lambda x:-x[1])
    print(word_count,sortedWords)
    k=2
    return sortedWords[:k][0]

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit ha ha ha."
banned = ["hit"]
print( mostCommonWord(paragraph,banned))