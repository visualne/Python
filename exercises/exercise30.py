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
        self.tail = None

def print_singly_linked_list(node, sep):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtHead(llist, data):

    #  Write your code here

    #  First pass data is 383 and llist is None - 383 is returned
    if llist is None:
        #  Creating new node with data value.
        node = SinglyLinkedListNode(data)
        #  Adding data to llist.head
        llist.head = node

        #  Returning llist.head
        return llist.head

    #  Second pass data is 484 and llist is 383 - 484 is returned
    #  Third pass data is 392 and llist is 484 - 392 is returned
    #  Fourth pass data is 975 and llist is 392 - 975 is returned
    #  Fifth pass data is 321 and llist is 321 - 321 is returned

# Input
# 383
# 484
# 392
# 975
# 321

# Output
# 321
# 975
# 392
# 484
# 383

    #  Return new head node everytime.

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # llist_count = int(input())
    llist_count = [383,484,392,975,321]

    llist = SinglyLinkedList()
    #
    for val in llist_count:
        llist_item = val
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head
    #
    # print_singly_linked_list(llist.head, '\n')
    # fptr.write('\n')
    #
    # fptr.close()