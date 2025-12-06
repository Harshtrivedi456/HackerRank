#!/bin/python3

import math
import os
import random
import re
import sys

def introTutorial(V, arr):
    return arr.index(V)

if __name__ == '__main__':
    V = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(introTutorial(V, arr))
