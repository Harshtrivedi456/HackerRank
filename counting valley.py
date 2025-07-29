#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    level = 0       # Current level
    valleys = 0     # Count of valleys

    for i in range(steps):
        if path[i] == 'U':
            level += 1
            if level == 0:
                valleys += 1
        elif path[i] == 'D':
            level -= 1
        else:
            return -1   # Invalid character

    return valleys

steps = int(input())
path = input()

print(countingValleys(steps, path))
