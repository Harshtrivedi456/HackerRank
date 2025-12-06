#!/bin/python3

import sys

def hackerrankInString(s):
    target = "hackerrank"
    i = 0
    for c in s:
        if c == target[i]:
            i += 1
            if i == len(target):
                return "YES"
    return "NO"

if __name__ == "__main__":
    q = int(sys.stdin.readline())
    for _ in range(q):
        s = sys.stdin.readline().strip()
        print(hackerrankInString(s))
