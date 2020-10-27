#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 15:21:43 2020

@author: Suma


"""

def riverSizes(matrix):
	result = []
	visited = [[False for value in row] for row in matrix]
	
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			if visited [i][j]:
				continue
			traverseNode(i,j,matrix,visited,result)
	return result

def traverseNode(i,j,matrix,visited,result):
	riverSize = 0
	stack = [[i,j]]
	
	while stack:
		node = stack.pop()
		i, j = node[0], node[1]
		
		if visited[i][j]:
			continue
		visited[i][j] = True
		
		if matrix[i][j] == 0 :
			continue
			
		riverSize += 1
		
		unvisited = getUnVisited(i,j,matrix,visited)
		
		for grid in unvisited:
			stack.append(grid)
			
	if riverSize > 0:
		result.append(riverSize)
				
def getUnVisited(i,j,matrix,visited):
    
	unvisited=[]
    
	if not visited[i-1][j] and i>0:
		unvisited.append([i-1, j])
        
	if  i < len(matrix)-1 and not visited[i+1][j]:
		unvisited.append([i+1, j])
	
	if not visited[i][j-1] and j>0:
		unvisited.append([i, j-1])
        
	if  j < len(matrix[0])-1 and not visited[i][j+1]:
		unvisited.append([i, j+1])
	
	return unvisited

matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]
print(riverSizes(matrix))