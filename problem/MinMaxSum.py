#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    minimum = 0
    maximum = 0
    for i in range(len(arr)):
        total = 0
        j = 0
        while j < len(arr):
            if i == j:
                j = j + 1
                continue
            total = total + arr[j]
            j = j + 1
        if i == 0:
            minimum = total
            maximum = total
        else:
            if total < minimum:
                minimum = total
            if total > maximum:
                maximum = total

    print(minimum, maximum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
