#!/usr/bin/env python3

def beautifulBinaryString(b):
    count = 0
    i = 0
    while i < len(b) - 2:
        if b[i:i+3] == "010":
            count += 1
            i += 3   # skip this pattern
        else:
            i += 1
    return count

if __name__ == '__main__':
    n = int(input().strip())
    b = input().strip()
    print(beautifulBinaryString(b))
