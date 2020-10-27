#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 14:09:58 2020

@author: SujithPatnaik

Algorithm:
    
Created a stack of nodes and visited array.
Insert the root in the stack.
Run a loop till the stack is not empty.
Pop the element from the stack and print the element.
For every adjacent and unvsisted node of current node, mark the node and insert it in the stack.
Implementation of Iterative DFS: This is similar to BFS, the only difference is queue is replaced by stack.

"""

# An Iterative Python 3 program to do DFS  
# traversal from a given source vertex.  
# DFS(s) traverses vertices reachable from s. 
class Graph:  
    def __init__(self, V): 
        self.V = V  
        self.adj = [[] for i in range(V)]  #adjacency neighbours lists or child nodes
      
    def addEdge(self, v, w): 
        self.adj[v].append(w) # Add w to v’s list. 
      
    # prints all not yet visited vertices  
    # reachable from s  
    def DFSUtil(self, node, visited): 
          
        # Create a stack for DFS  
        stack = [] 
      
        # Push the current source node/root.  
        stack.append(node)  
      
        while stack: 
              
            # Pop a vertex from stack and print it  
            node = stack.pop() 
      
            # Stack may contain same vertex twice.  
            # So we need to prthe popped item only  
            # if it is not visited.  
            if (not visited[node]): 
                print(node, end = " ")  
                visited[node] = True
      
            # Get all adjacent vertices of the  
            # popped vertex s. If a adjacent has not   
            # been visited, then push it to the stack. 
            i = 0
            for i in range(len(self.adj[node])): 
                if (not visited[self.adj[node][i]]):  
                    stack.append(self.adj[node][i]) 
                i += 1
      
    # prints all vertices in DFS manner  
    def DFS(self): 
          
        # Mark all the vertices as not visited  
        visited = [False] * self.V 
        for i in range(self.V): 
            if (not visited[i]): 
                self.DFSUtil(i, visited) 
  
# Driver Code 
if __name__ == '__main__': 
  
    g = Graph(5) # Total 5 vertices in graph  
    g.addEdge(1, 0)  
    g.addEdge(2, 1)  
    g.addEdge(3, 4)  
    g.addEdge(4, 0)  
  
    print("Following is Depth First Traversal")  
    g.DFS()