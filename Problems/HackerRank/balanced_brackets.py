#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    if len(s) == 1:
        return 'NO'
    my_stack = []
    for char in s:
        
        if len(my_stack) == 0 and char not in ['(', '[', '{']:
            return 'NO'
        if char in ['(', '[', '{']:
            my_stack.append(char)
        elif char == ')' and my_stack[-1] == '(':
            my_stack.pop()
        elif char == ']' and my_stack[-1] == '[':
            my_stack.pop()
        elif char == '}' and my_stack[-1] == '{':
            my_stack.pop()
        else:
            return 'NO'

    return 'NO' if my_stack else 'YES'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
