
import math
import os
import random
import re
import sys
from turtle import position

from attr import validate

# Complete the minimumSwaps function below.


def swap(a, b, arr, posArr):

    valA = arr[a]
    valB = arr[b]

    arr[a] = valB
    arr[b] = valA

    posArr[valA-1] = posArr[a]


def minimumSwaps(arr):
    swapCount = 0
    mainIndex = 0
    sortedArr = sorted(arr)
    positionArr = [None for x in range(len(arr))]
    for i in range(len(arr)):
        positionArr[arr[i]-1] = i

    print(arr)
    for i in range(len(arr)-1):
        if arr[i] != i+1:

            # print("swapping {} with {} , arr {}, posArr {}".format(
            #     i, positionArr[i], arr, positionArr))

            swap(i, positionArr[i], arr, positionArr)

            # print("                    arr {} , posArr {}\n====".format(
            #     arr, positionArr))

            swapCount += 1

    return swapCount
    # positionArr.pop(0)
    # print(positionArr)

# while mainIndex < len(arr)-1:

# if posDict.keys()[0]==mainIndex:

# while mainIndex < len(arr)-1:
#     currMinVal = arr[mainIndex]
#     currMinInd=mainIndex
#     for i in range(mainIndex+1, len(arr)):
#         if currMinVal > arr[i]:
#             currMinInd = i
#             currMinVal=arr[i]
#     if currMinInd != mainIndex:
#         swap(mainIndex, currMinInd, arr)
#         swapCount+=1
#         print("swapping {} with {} , dynlist {}".format(mainIndex,currMinInd,arr))
#     mainIndex+=1
# return swapCount


arr = [7, 1, 3, 2, 4, 5, 6]
# arr = [2, 3, 4, 1, 5]
print(minimumSwaps(arr))
