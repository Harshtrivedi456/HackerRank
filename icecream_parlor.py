#!/bin/python3

import math
import os
import random
import re
import sys

def icecreamParlor(m, arr):
    seen = {}
    for i, price in enumerate(arr):
        needed = m - price
        if needed in seen:
            return [seen[needed] + 1, i + 1]
        seen[price] = i

if __name__ == '__main__':
    t = int(sys.stdin.readline())
    for _ in range(t):
        m = int(sys.stdin.readline())
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        result = icecreamParlor(m, arr)
        print(*result)
