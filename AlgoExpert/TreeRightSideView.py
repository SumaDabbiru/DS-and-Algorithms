#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 21:39:19 2020

@author: SujithPatnaik
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        output = []
        next_level = collections.deque([root,])

        while next_level:
            
            current_level = next_level
            next_level = deque()
            
            while current_level:
                node = current_level.popleft()
                
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
                
            output.append(node.val)              
        return output