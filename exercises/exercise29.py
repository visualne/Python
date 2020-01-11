#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

def print_singly_linked_list(node, sep):
    while node:
        # fptr.write(str(node.data))
        print node.data

        node = node.next

        # if node:
        #     fptr.write(sep)

# Complete the insertNodeAtTail function below.

# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):

    #  141 > Null
    #  141 > 302 > Null
    #  141 > 302 > 164 > Null
    #  141 > 302 > 164 > 530 > Null

    #  Need a way to traverse list every time
    #  this function is called and get to node with
    #  a pointer of null. Once you are there you want
    #  to insert the data that was sent in.

    #  Maybe for loop that says something like, while node.next is not null
    #  go to next node, (node = node.next)
    #    set node = node.next
    #  when null is found. Insert data at node.next and return head

    if head == None:
        head = SinglyLinkedListNode(data)
        head.next = None
    else:
        #  This if statement deals with cases where head.next is None.
        if head.next == None:
            head.next = SinglyLinkedListNode(data)
            return head

        #  Setting head.next equal to the node value.
        node = head.next

        #  This while look gets to the end of the list.
        #  In other words a node that has a next value set to None.
        while node.next != None:
            node = node.next
        #  Setting node.next appropriately.
        node.next = SinglyLinkedListNode(data)

    #  Returning head node.
    return head



    #  First pass 141 will be sent in with a pointer to Null
    #  Second pass 302 will be sent in with a pointer to null, 141 will point
    #  to 302.

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # llist_count = int(input())

    llist = SinglyLinkedList()

    sample_list = [141,302,164,530,474]

    # for i in range(llist_count):
    #     llist_item = int(input())
    #     llist_head = insertNodeAtTail(llist.head, llist_item)
    #     llist.head = llist_head

    for i in sample_list:
        llist_item = i
        llist_head = insertNodeAtTail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n')
    # fptr.write('\n')

    # fptr.close()
