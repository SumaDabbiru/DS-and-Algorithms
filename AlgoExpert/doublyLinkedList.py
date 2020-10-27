
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class LinkedList:
    # Function to initialize the Linked
    # List object
    def __init__(self):
        self.head = None

    def __init__(self):
        self.tail = None


    def printList(self):
        temp = self.head
        while (temp):
            print(temp.val)
            temp = temp.next

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.


        if index < 0 or index >= self.size:
            return -1
        """
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp.val

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0:
            return 0
        # if index > self.size:
        #     return
        temp = self.head

        for _ in range(index):
            temp = temp.next

        second = temp.next

        # self.size += 1
        valueadded = Node(val)
        temp.next = valueadded
        valueadded.next = second

    def addAtHead(self, val: int) -> None:
        new1 = Node(val)
        if self.head is None:
            self.head =node
            self.tail =node
            return
        self.insertBefore(self.head,node)

    def addAtTail(self, node) -> None:
        if self.tail is None:
            self.head(node)
            return
        self.insertAfter(self.tail,node)


    def deleteAtIndex(self, index: int) -> None:
        print("in delete")

        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return 0
        temp = self.head
        for _ in range(inde x -1):
            temp = temp.next
        if temp.next is not None:
            temp.next = temp.next.next

    def insertBefore(self ,node ,nodetoinsert):
        pass

    def insertAfter(self ,node ,nodetoinsert):
        pass

    def insertAtPosition(self ,position ,nodetoinsert):
        pass
    def removeNodeswithValue(self ,value):
        pass
    def remove(self ,node):
        pass
    def containesNodeswithValues(self ,value):
        pass
    def removenodeBindings(self, value):



if __name__ == '__main__':
    # Start with the empty list
    llist = LinkedList()

    llist.head = Node(1)
    second = Node(2)
    third = Node(3)

    llist.head.next = second;  # Link first node with second
    second.next = third;  # Link second node with the third node

    llist.printList()
    # print(llist.addAtIndex(1,5))
    # print(llist.addAtHead(9))
    # print(llist.get(2))

    # print(llist.addAtTail(9))
    print(llist.deleteAtIndex(1))
    print(llist.get(0))
    print(llist.get(1))
    print(llist.get(2))



# class LinkedList:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.size = 0
#         self.head = ListNode(0)
#
#     def get(self, index: int) -> int:
#         print("in get")
#         """
#         Get the value of the index-th node in the linked list. If the index is invalid, return -1.
#         """
#         temp = self.head
#         if index < 0 or index >= self.size:
#             return -1
#         for i in range(index + 1):
#             temp = temp.next
#         return temp.val
#

#         """
#         Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
#
#         """
#
#     def addAtTail(self, val: int) -> None:
#         print("in addattail")
#         self.addAtIndex(self.size, val)
#         """
#         Append a node of value val to the last element of the linked list.
#
#         """
#

#
