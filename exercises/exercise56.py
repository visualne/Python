#!/bin/python3

import math
import os
import random
import re
import sys

def Convert_to_dict(lst):

    words_dictionary = {}

    #  Creating words dictionary
    for val in lst:
        if val in words_dictionary:
            words_dictionary[val] = words_dictionary[val] + 1
        else:
            words_dictionary[val] = 1

    #  Returning dictionary
    return words_dictionary

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    magazineDict = Convert_to_dict(magazine)
    noteDict = Convert_to_dict(note)

    for word in noteDict.keys():
        if word in magazineDict.keys():
            #  Check to see if nuumber of words is >=1
            #  if it is the counter will be decremented.
            if magazineDict[word] >= noteDict[word]:
                found = True
            #  This else path means the the word appears
            #  more times in note than it does in the magazine.
            else:
                found = False
                break
        else:
            found = False
            break

    if found:
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    # mn = input().split()

    # m = int(mn[0])
    #
    # n = int(mn[1])

    m = 'two times three is not four'

    n = 'two times two is four'

    magazine = m.rstrip().split()

    note = n.rstrip().split()

    checkMagazine(magazine, note)
