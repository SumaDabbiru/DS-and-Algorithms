#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 21:00:58 2020

@author: SujithPatnaik
"""

class ancesteralTree():
    def __init__(self,name):
        self.name = name
        self.ancestor = None

def youngAncestor(topA, D1, D2):
    #topA = topAncestoral
    #D1 = decendant1, D2 = decendant2
    depth1 = decendantdepth(D1, topA)
    depth2 = decendantdepth(D2, topA)
    
    if depth1 > depth2:
        return backtracking(depth1, depth2, depth1 - depth2)
    else:
        return backtracking(depth2, depth1, depth2 - depth1)
 

def decendantdepth(decendant, topA):
    depth =0
    while decendant != topA:
        depth += 1
        decendant = decendant.ancestor
    return depth

def backtracking(lowerD, higherD, diff):
    while diff > 0:
        lowerD = lowerD.ancestor
    while lowerD != higherD:
        lowerD = lowerD.ancestor
        higherD = higherD.ancestor
    return lowerD

        