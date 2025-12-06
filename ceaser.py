#!/bin/python3

import sys

def caesarCipher(s, k):
    res = []
    k %= 26
    for c in s:
        if 'a' <= c <= 'z':
            res.append(chr((ord(c) - ord('a') + k) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            res.append(chr((ord(c) - ord('A') + k) % 26 + ord('A')))
        else:
            res.append(c)
    return "".join(res)

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    k = int(sys.stdin.readline())
    print(caesarCipher(s, k))
