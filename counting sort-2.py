#!/bin/python3

import sys

def countingSort(arr):
    count = [0] * 100
    for x in arr:
        count[x] += 1
    result = []
    for i in range(100):
        result.extend([i] * count[i])
    return result

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(*countingSort(arr))
