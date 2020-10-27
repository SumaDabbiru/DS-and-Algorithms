#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:56:01 2020

@author: SujithPatnaik
"""
# time o(n^2) spance o(n^2)

def fourNumberSum(array, targetSum):
    # Write your code here.
    allPairSum = {}
    result = []
    
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            currentSum = array[i] + array[j]
            difference = targetSum - currentSum
            if difference in allPairSum:
                for pair in allPairSum[difference]:
                    result.append(pair + [array[i],array[j]])
        for k in range(0,i):
            currentSum = array[i] + array[k]
            if currentSum not in allPairSum:
                allPairSum[currentSum] = [[array[i],array[k]]]
            else:
                allPairSum[currentSum].append([array[i],array[k]])
    return result
                
                 
            
                
        
        
    pass

array= [7, 6, 4, -1, 1, 2]
target = 16
print(fourNumberSum(array, target))