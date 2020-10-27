#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 22:03:00 2020

@author: SujithPatnaik
"""

# time: O(n) Space O(n)
def zigzagTraverse(matrix):
    
    row = col = 0
    result = []
    R = len(matrix)-1
    C = len(matrix[0])-1
    goingdown = True
    
    while not outofbounds(row,col,R,C):
        
        result.append(matrix[row][col])
        
        if goingdown:
            
            if col == 0 or row == R:
                goingdown = False
                if row == R:
                    col += 1
                else:
                    row += 1
            else:
                row += 1
                col -= 1
        else:
            if row==0 or col == C:
                goingdown = True
                
                if col == C:
                    row+=1
                else:
                    col+=1
            else:
                row -= 1
                col += 1
    return result
    
    
    pass

def outofbounds(row,col,R,C):
    return row < 0 or row > R or col < 0 or col > C

matrix = [[1, 3, 4, 10], [2, 5, 9, 11], [6, 8, 12, 15], [7, 13, 14, 16]]

print(zigzagTraverse(matrix))