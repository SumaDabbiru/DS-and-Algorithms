#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 15:02:34 2020

@author: SujithPatnaik
"""
class Node():

	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None
		self.parent = None
		

class Tree():
    def hasPathSum(self, root, sum):
        if not root:
            return False

        de = [(root, sum - root.val), ]
        while de:
            node, curr_sum = de.pop()
            if not node.left and not node.right and curr_sum == 0:  
                return True
            if node.right:
                de.append((node.right, curr_sum - node.right.val))
            if node.left:
                de.append((node.left, curr_sum - node.left.val))
        return False
    def __init__(self):
        self.root = None	
        pass
    
    def add_node(self,key,node=None):
        if node is None:
            node = self.root
        if self.root is None:
            self.root = Node(key)
        else:
            if key <= node.key :
                if node.left is None:
                    node.left = Node(key)
                    node.left.parent = node
                    return
                else:
                    # return self.add_node(key,node = self.root.left)
                    return self.add_node(key,node = node.left)
            else:
                if node.right is None:
                    node.right = Node(key)
                    node.right.parent = node
                    return
                else:
                    # return self.add_node(key,node = self.root.right)
                    return self.add_node(key,node = node.right)

t=Tree()
t.add_node(10)
t.add_node(13)
t.add_node(14)
t.add_node(8)
t.add_node(9)
t.add_node(7)
t.add_node(11)
print(t.hasPathSum(Tree().root, 0))

'''
10---8---7
  |	 |
  |	 ---9
  ---13---11
  	   |
  	   ---14	
'''
"""
null = None

"nodes":[
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "5", "left": "10", "right": null, "value": 5},
    {"id": "6", "left": null, "right": null, "value": 6},
    {"id": "7", "left": null, "right": null, "value": 7},
    {"id": "8", "left": null, "right": null, "value": 8},
    {"id": "9", "left": null, "right": null, "value": 9},
    {"id": "10", "left": null, "right": null, "value": 10}
    ]
"root": "1"

print(Solution().hasPathSum(key, sum))
"""