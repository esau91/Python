#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Write your code here
    my_words = {}
    
    if len(note) > len(magazine):
        print('No')
        return 0
    
    for word in note:
        if word not in my_words:
            my_words[word] = 1
        else:
            my_words[word] += 1

    for word in magazine:
        if word in my_words and my_words[word] >= 1:
            my_words[word] -= 1

    if sum(my_words.values()) == 0:
        print('Yes')
        return 0
    else:
        print('No')
        return 0
        
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
