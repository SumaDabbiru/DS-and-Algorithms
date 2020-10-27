#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:13:29 2020

@author: SujithPatnaik
"""

def cycleCheck(array):
    visited = 0
    currentIdx = 0
    nextIdx = 0
    
    while visited < len(array):
        if visited > 0 and currentIdx == 0: #rotating in circles
            return False
        
        visited += 1
        
        nextIdx = (currentIdx + array[currentIdx]) % len(array)
        
        if nextIdx >= 0:
            currentIdx = nextIdx
        else:
            currentIdx = nextIdx + len(array)
    return currentIdx == 0
    pass

array = [2, 3, 1, -4, -4, 2]
# {"array": [0, 1, 1, 1, 1]} O/p False
print(cycleCheck(array))