#!/bin/python3

import sys

def marsExploration(s):
    expected = "SOS" * (len(s) // 3)
    return sum(1 for a, b in zip(s, expected) if a != b)

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    print(marsExploration(s))
