#!/bin/python

import math
import os
import random
import re
import sys
# from __future__ import print_function

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
# def printLinkedList(head):
#     pass

if __name__ == '__main__':
    # llist_count = int(raw_input())
    llist_count = [3,5,2,5,3]

    llist = SinglyLinkedList()

    # for  in xrange(llist_count):
    #     llist_item = int(raw_input())
    #     llist.insert_node(llist_item)

    # for  in xrange(llist_count):
    #     llist_item = int(raw_input())
    for val in llist_count:
        llist.insert_node(val)

    # printLinkedList(llist.head)