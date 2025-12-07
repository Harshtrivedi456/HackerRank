#!/bin/python3

import sys

def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

if __name__ == "__main__":
    q = int(sys.stdin.readline())
    for _ in range(q):
        s = sys.stdin.readline().strip()
        print(alternatingCharacters(s))
