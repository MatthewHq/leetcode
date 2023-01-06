#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stepPerms' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def stepPerms(n):
    # Write your code here
    return stepCounts(n, 0)


def stepCounts(n, step):
    base=[1,1,2,4]
    if n<4:
        return base[n]
    else:
        steps=4
        for i in range(3,n):
            # print(i)
            steps*=2
            # print(steps)
            steps-=base[i-3]
            # print(steps)
            base.append(steps)
            # print(base)
        return steps



for i in range(14):
    print(stepPerms(i))


# print(stepPerms(5))
