#!/bin/python3

import sys

def insertionSort1(n, arr):
    x = arr[-1]
    i = n - 2
    while i >= 0 and arr[i] > x:
        arr[i + 1] = arr[i]
        print(*arr)
        i -= 1
    arr[i + 1] = x
    print(*arr)

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    insertionSort1(n, arr)
