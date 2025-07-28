#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#
def birthday(s, d, m):
    count = 0
    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1
    return count

# Input Section
n = int(input())                         # total number of squares
s = list(map(int, input().split()))     # the chocolate bar with integers
d, m = map(int, input().split())        # Ron's birth day and month

# Output the result
print(birthday(s, d, m))
    
