#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:20:22 2020

@author: SujithPatnaik
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        if self.head is None:
            self.head = node
        else:
            self.insertBefore(self.head,node)
        return

    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail,node)
        return

        pass

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head or nodeToInsert == self.tail:
            self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next=node
        if node.prev == None:
            self.head = nodeToInsert
        else:
            node.prev.next  =  nodeToInsert
        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head or nodeToInsert == self.tail:
            self.remove(nodeToInsert)
        nodeToInsert.next=node.next
        nodeToInsert.prev = node
        
        if node.next == None:
            self.tail = nodeToInsert
        else:
            node.next.prev  =  nodeToInsert
        node.next = nodeToInsert
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        if position == 1:
            self.head(nodeToInsert)
            return
        node = self.head
        currentPosition = 1
        while node is not None and currentPosition != position:
            node = node.next
            currentPosition += 1
        if node is not None:
            self.insertBefore(node,nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    def removeNodesWithValue(self, val):
        # Write your code here.
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if nodeToRemove.val == val:
                self.remove(nodeToRemove)
        pass

    def remove(self, node):
        # Write your code here.
        if node == self.head:
            self.head = self.head.next
        elif node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBinding(node)
        
    def removeNodeBinding(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev  =node.prev
        node.prev = None
        node.next = None

    def containsNodeWithValue(self, val):
        # Write your code here.
        node = self.head
        while node is not None and node.val != val:
            node = node.next
        return node is not None
                
    def removeKthNodeFromEnd(head,k):
        node = head
        for _ in range(k):
            node = node.next
        temp = head
        if node is None: #kth node is head
            self.head.value = head.next.val
            head.next = head.next.next
        while node is not None:
            node = node.next
            temp = temp.next
        temp.next= temp.next.next