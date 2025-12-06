#!/bin/python3

import math
import os
import random
import re
import sys

def bigSorting(unsorted):
    return sorted(unsorted, key=lambda x: (len(x), x))

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = [sys.stdin.readline().strip() for _ in range(n)]
    result = bigSorting(arr)
    print("\n".join(result))
