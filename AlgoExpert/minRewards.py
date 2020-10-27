#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:10:52 2020

@author: SujithPatnaik

Min rewards given to studnts with provided scores. 2 conditions
1. everyone should get one
2. more score that adjacent should get more rewards
"""

def minRewards(scores):
    rewards = [1 for _ in scores]
    
    for i in range(1,len(scores)):
        j = i - 1
        #if the student got more than before student add the reward
        if scores[i] > scores[j]:
            rewards[i] = rewards[j]+1
        
        # if the before students score is more than the current student 
        #traverse back to update the rewards 
        #else:
            #while j >= 0 and scores[j] > scores[j+1]:
                #rewards[j] = max(rewards[j], rewards[j+1]+1)
                #j-=1
    # or we can traverse back again at once to update the scores
    for i in reversed(range(len(scores)-1)):
        #j = i + 1
        
        if scores[i] > scores[i+1]:
            rewards[i] = max(rewards[i], rewards[i+1]+1)
        
        
    print(rewards)
    return sum(rewards)
        
    
    pass

scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))