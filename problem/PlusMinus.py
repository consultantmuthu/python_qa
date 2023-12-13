#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    result = [0,0,0]
    length = len(arr)    
    for data in arr:
        if data > 0:
            result[0] = result[0] + 1 
        if data < 0:
            result[1] = result[1] + 1
        if data == 0:
            result[2] = result[2] + 1
    print('{0:.6f}'.format(result[0]/length))
    print('{0:.6f}'.format(result[1]/length))
    print('{0:.6f}'.format(result[2]/length))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
