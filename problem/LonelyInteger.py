#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    counter = {}
    for i in a:
        value = counter.get(i, 0) + 1
        counter[i] = value
    for key, value in counter.items():
        if value == 1:
            return key

if __name__ == '__main__':
    a = [1,2,3,4,1,2,3]
    lonelyinteger(a)