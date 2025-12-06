#!/bin/python3

import sys

def quickSort(arr):
    pivot = arr[0]
    left = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return left + equal + right

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    result = quickSort(arr)
    print(*result)
