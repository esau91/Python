#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):
    # Write your code here
    count = 0
    a_count = 0
    b_count = 0
    for char in s:    
        if char == 'A':
            if b_count > 1:
                count += b_count - 1
            a_count += 1
            b_count = 0
        elif char == 'B':
            if a_count > 1:
                count += a_count - 1
            b_count += 1
            a_count = 0
        
    if a_count > 1:
        count += a_count - 1
    if b_count > 1:
        count += b_count - 1
        
    return count 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
