#!/bin/python3

import math
import os
import random
import re
import sys

def camelcase(s):
    return 1 + sum(1 for c in s if c.isupper())

if __name__ == '__main__':
    s = sys.stdin.readline().strip()
    print(camelcase(s))
