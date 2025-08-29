import math
import os
import random
import re
import sys



def plusMinus(arr, size):
    posicount = 0
    negcount = 0
    zero = 0

    for num in arr:
        if num < 0:
            negcount += 1
        elif num > 0:
            posicount += 1
        else:
            zero += 1

    positive = posicount / size
    negative = negcount / size
    zeros = zero / size

    print(f"{positive:.6f}")
    print(f"{negative:.6f}")
    print(f"{zeros:.6f}")


size = int(input())
arr = list(map(int, input().split()))
plusMinus(arr, size)


        
    
        
        
        
         
