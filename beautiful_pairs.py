#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def beautifulPairs(A, B):
    c1 = Counter(A)
    c2 = Counter(B)
    common = sum((c1 & c2).values())

    if common < len(A):
        return common + 1
    else:
        return common - 1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    print(beautifulPairs(A, B))
