#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def makeAnagram(a, b):
    # Write your code here
    my_words = {}
    for word in a:
        if word in my_words:
            my_words[word] += 1
        else:
            my_words[word] = 1
 
    for word in b:
        if word in my_words:
            my_words[word] -= 1
        else:
            my_words[word] = -1

    my_sum = sum(abs(number) for number in list(my_words.values()))
    return my_sum
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
