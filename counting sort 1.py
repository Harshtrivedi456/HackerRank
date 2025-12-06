#!/bin/python3

import sys

def countingSort(arr):
    count = [0] * 100
    for num in arr:
        count[num] += 1
    return count

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    print(*countingSort(arr))
