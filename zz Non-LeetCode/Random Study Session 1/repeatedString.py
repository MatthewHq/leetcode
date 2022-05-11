#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Write your code here
    aPoints = []
    count = 0
    for c in s:
        if c == 'a':
            count += 1
        aPoints.append(count)
    sLen = len(s)
    remainder = n % sLen
    divided = int(n/sLen)
    print("slen:{} int(n/sLen):{} int(n/sLen)*count:{}, divided:{}, remainder{}, count:{}".format(sLen,
          divided, divided*count, divided, remainder, count))

    totA=int(n/sLen)*count

    if(remainder!=0):
        totA+=aPoints[remainder-1]

    return totA

    # totA=int(n/sLen)*count+aPoints[remainder-1]
    # return int(n/sLen)*count if divided < 1 or remainder == 0 else int(n/sLen)*count+aPoints[remainder-1]
    


s = 'abcac'


print(repeatedString(s, 5))
print(repeatedString(s, 8))

s = 'a'
print(repeatedString(s, 1000000000000))

s = 'ababa'
print(repeatedString(s, 3))
