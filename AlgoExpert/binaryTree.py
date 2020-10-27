#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 15:16:06 2020

@author: SujithPatnaik
"""
class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):

    def __init__(self, root):
        self.root = Node(root)
    

    def length(self):
        return self.size
    
    def search(self,root,val): 
      
    # Base Cases: root is null or key is present at root 
        if root is None or root.val == val: 
            return root 
  
    # Key is greater than root's key 
        if root.val < val: 
            return self.search(root.right,val) 
    
    # Key is smaller than root's key 
        return self.search(root.left,val)
    
    def insert(self,value): 
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                else:
                    currentNode = currentNode.right
                
            
    def inorder(self,root,result): 
        # left-Root-Right
        
        if root: 
            result = self.inorder(root.left,result) 
            result.append(root.value) 
            result = self.inorder(root.right, result) 
        return result
        

    
    def preOrderPrint(self, start, traversal):
        #root-Left-Right        
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preOrderPrint(start.left, traversal)
            traversal = self.preOrderPrint(start.right, traversal)
        return traversal
    
    def postorder(self,root,result): 
        # left-Right-Root
  
        if root: 
            result = self.postorder(root.left,result) 
            result = self.postorder(root.right, result)
            result.append(root.value) 
        return result
    
    def printTree(self, traversalType):
        if traversalType == "preorder":
            return self.preOrderPrint(r.root,"")
        
        elif traversalType == "inorder":
            return self.inorder(r.root,[])
        
        elif traversalType == "postorder":
            return self.postorder(r.root,[])
        
        else:
            print("invalid traversal")

# Driver program to test the above functions 
# Let us create the following BST 
#        1 
#     /      \ 
#    2       3 
#   / \     /  \ 
#  4  5    6   7 
'''

'''
r = BinaryTree(1)
r.root.left = Node(2)
r.root.right = Node(3)
r.root.left.left = Node(4)
r.root.left.right = Node(5)
r.root.right.left = Node(6)
r.root.right.right = Node(7)
  
# Print inoder traversal of the BST 
print(r.printTree("preorder"))
print(r.printTree("inorder"))

print(r.printTree("postorder"))
