#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 13:53:42 2020

@author: SujithPatnaik

import program
import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(program.branchSums(tree), [15, 16, 18, 10, 11])

"""


class BinaryTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self
    
    def branchSums(root):
        sums = []
        BinaryTree().calculateBranchSum(root, 0, sums)
        return sums
    
    
    def calculateBranchSum(node, currentSum, sums):
        if node is None:
            return
        newsum = currentSum + node.value
        if node.left is None and node.right is None:
            sums.append(newsum)
            
            return
        
        BinaryTree().calculateBranchSum(node.left, newsum, sums)
        BinaryTree().calculateBranchSum(node.right, newsum, sums)
    
t = BinaryTree("1")
t.insert([1])


print(BinaryTree("1").branchSums(BinaryTree(1)))



