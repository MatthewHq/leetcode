#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    totMax=0
    biggestSums=[0 if arr[0]<0 else arr[0]]
    if biggestSums[0]>arr[1]:
        biggestSums.append(biggestSums[0])
    else:
        biggestSums.append(0 if arr[1]<0 else arr[1])
    
    for i in range(2,len(arr)):
        current=0 if arr[i]<0 else arr[i]
        # print(current)
        tMax=max(current+biggestSums[i-2],biggestSums[i-1])
        if tMax>totMax:
            totMax=tMax
        biggestSums.append(tMax)
    print(biggestSums)
    return totMax
    


arr=[1,-2,1,3,-4,5]
# arr=[-2,1,5,10,6,-1,4,-1,-1,-1]
# arr=[-1,-1,-1,-1,1,-1,1,-1,0,1,1,1]
# arr=[3,5,-7,8,10]
print(maxSubsetSum(arr))
