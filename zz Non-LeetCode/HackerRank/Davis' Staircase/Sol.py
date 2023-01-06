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
    if step == n:
        return 1
    else:
        paths = stepCounts(n, step+1)
        if step+2 <= n:
            paths += stepCounts(n, step+2)
        if step+3 <= n:
            paths += stepCounts(n, step+3)
        return paths


for i in range(14):
    print(stepPerms(i))

