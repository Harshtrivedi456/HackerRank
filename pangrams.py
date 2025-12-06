#!/bin/python3

import sys

def pangrams(s):
    s = s.lower()
    return "pangram" if set("abcdefghijklmnopqrstuvwxyz") <= set(s) else "not pangram"

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(pangrams(s))
