#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#
def countApplesAndOranges(s, t, a, b, apples, oranges): 
    apple_count = 0
    orange_count = 0

    for d in apples:
        if s <= a + d <= t:
            apple_count += 1

    for d in oranges:
        if s <= b + d <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)

# Read input from stdin as expected by HackerRank
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

countApplesAndOranges(s, t, a, b, apples, oranges)
