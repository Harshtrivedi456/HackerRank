#!/bin/python3

import sys
import re

def minimumNumber(n, password):
    count = 0
    if not re.search(r'[0-9]', password): count += 1
    if not re.search(r'[a-z]', password): count += 1
    if not re.search(r'[A-Z]', password): count += 1
    if not re.search(r'[^a-zA-Z0-9]', password): count += 1
    return max(count, 6 - n)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    password = sys.stdin.readline().strip()
    print(minimumNumber(n, password))
