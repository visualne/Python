#!/bin/python

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
        # fptr.write(str(node.data))
        print node.data
        print sep
        node = node.next

        # if node:
        #     fptr.write(sep)

# Complete the insertNodeAtHead function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next


def insertNodeAtHead(llist, data):
    #  Write your code here
    #  Will return an object of type SinglyLinkedListNode
    node = SinglyLinkedListNode(data)
    node.next = llist

    return node

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    elementsList = [383,484,392,975,321]

    # llist_count = int(raw_input())

    llist = SinglyLinkedList()

    for llist_item in elementsList:
        # llist_item = int(raw_input())
        llist_head = insertNodeAtHead(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n')
    # fptr.write('\n')
    #
    # fptr.close()
