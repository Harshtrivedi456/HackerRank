#!/bin/python3

import sys

def funnyString(s):
    r = s[::-1]
    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(r[i]) - ord(r[i-1])):
            return "Not Funny"
    return "Funny"

if __name__ == "__main__":
    q = int(sys.stdin.readline())
    for _ in range(q):
        s = sys.stdin.readline().strip()
        print(funnyString(s))
