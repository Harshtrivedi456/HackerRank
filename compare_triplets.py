#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    count1 = 0
    count2 = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            count1 += 1
        elif a[i] < b[i]:
            count2 += 1
    return [count1, count2]  # moved outside loop

# take inputs
alice = list(map(int, input().split()))
bob = list(map(int, input().split()))

# call function and print result
result=compareTriplets(alice, bob)

print(result[0],result[1])

            
            
            
