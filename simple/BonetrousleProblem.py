#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
from array import array

#
# Complete the 'bonetrousle' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. LONG_INTEGER n
#  2. LONG_INTEGER k
#  3. INTEGER b
#

def bonetrousle(n, k, b):
    arr = []
    if k < b:
        arr.append(-1)
    else:
        if n > k:
            if n > ((k * b) - b):
                arr.append(-1)  
    data = itertools.permutations(range(k, k+b), b)
    for item in data:
        sum = 0
        for i in range(b):
            sum = sum + item[i]
        if (sum == n):
            #print(item)
            for j in range(b):
                arr.append(item[j])
            return arr
    return array("i", arr)

if __name__ == '__main__':
    '''
    result = bonetrousle(12, 8, 3)
    print(result)
    result = bonetrousle(10, 3, 3)
    print(result)
    result = bonetrousle(9, 10, 2)
    print(result)
    '''
    result = bonetrousle(999999995000050000, 10000000000000, 100000)
    print(result)

'''
963771 2314 1152
2722473 25433 560
20000000 20000000 6325
20000000 20000000 6324
20000000 10000000 4
20000000 10000000 3
20000000 10000001 2
20000000 10000000 2
20000000 10000000 1
20000000 20000000 5
20000000 20000000 4
20000000 20000000 3
20000000 20000000 2
20000000 20000000 1
19999650 20000000 6323
19999651 20000000 6324
19999649 20000000 6324
19999650 20000000 6325
19999650 20000000 6324
20000000 20000000 100000
'''