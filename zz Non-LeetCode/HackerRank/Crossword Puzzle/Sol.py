#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'crosswordPuzzle' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY crossword
#  2. STRING words
#

# word can be just "a" so type is ALL or None

# going with standalone recursion where we collected data via recursion just for the challenge
# i could have had an outside collection variable for alot of this stuff which I feel could be more efficient
# but we are studying recursion so going with this __add__ function to funnel all my data back up


# doing direction id
#

class wordSlot():
    def __init__(self):
        self.type = None
        self.end1 = None
        self.end2 = None
        # self.direction=None
        self.junctions = []

    def __add__(self, new):
        if self.end1 == None:
            self.end1 = new.end1
        if self.end2 == None:
            self.end2 = new.end
        for junction in new.junctions:
            self.junctions.append(junction)

    def __str__(self) -> str:
        return "Type "+str(self.type)+"\n"+"end1 "+str(self.end1)+"\n"+"end2 "+str(self.end2)+"\n"+"junctions "+str(self.junctions)


def crosswordPuzzle(crossword, words):
    visited = {}
    for x in range(10):
        for y in range(10):
            visited[(x, y)] = True
    print(visited)

    wordSlots = []
    while len(visited) > 0:
        coordTuple = visited.popitem()[0]
        print("popped",coordTuple)
        foundSlots = recursiveExplore(coordTuple, crossword, visited)
        if foundSlots != None:
            for wordSlot in foundSlots:
                wordSlots.append(wordSlot)
    print(visited)


def recursiveExplore(coords, crossword, visited, wordSlots=None, currentSlots=None):
    print("currentslots",currentSlots)
    # print(wordSlots)
    # print(wordSlots[1])
    # print(coords[0],coords[1])
    if crossword[coords[0]][coords[1]] == "-":
        if wordSlots == None:
            print("TRIGGERED")
            wordSlots = {1: wordSlot()}
            currentSlots = [1]
            currentSlot = wordSlots.get(1)
            for i in range(4):
                peekInto = move(coords, i)
                if visited.get(peekInto) != None and crossword[peekInto[0]][peekInto[1]] == "-":
                    currentSlot.type = i % 2
                    print("type found", i, coords)
                    break
            if currentSlot.type==None: 
                currentSlot.type =-1 #SINGLE LETTER WORD
                print("type found", -1, coords)
        for i in range(4):
            peekInto = move(coords, i)
            if visited.get(peekInto) != None and crossword[peekInto[0]][peekInto[1]] == "-":
                for currentSlotId in currentSlots:
                    currentSlot = wordSlots.get(currentSlotId)
                    if visited.get(peekInto)!=None:
                            del visited[peekInto]
                    if currentSlot.type != i % 2:
                        # new direction
                        print("NEW DIR EXPLORED",peekInto,currentSlotId,currentSlots)
                        newSlot=wordSlot()
                        newSlot.type=not currentSlot.type
                        wordSlots[len(wordSlots)+1]=newSlot
                        recursiveExplore(peekInto, crossword, visited, wordSlots, [len(wordSlots)+1])
                    else:
                        # same direction
                        print("SAME DIR EXPLORED",peekInto,currentSlotId,currentSlots)
                        recursiveExplore(peekInto, crossword, visited, wordSlots, [currentSlotId])
        

    else:
        return None

# 0 1 2 3 = down0 right1 up2 left3


def move(coord, direction):
    if direction == 0:
        return (coord[0]+1, coord[1])
    elif direction == 1:
        return (coord[0], coord[1]+1)
    elif direction == 2:
        return (coord[0]-1, coord[1])
    elif direction == 3:
        return (coord[0], coord[1]-1)
    return None  # shouldn't be reached


# reproducing hackerrank input
def input2Arr(input):
    arr = []
    arrList = input.split("\n")
    print(arrList)
    for line in range(len(arrList)-1):
        innerArr = []
        for char in range(len(arrList[line])):
            innerArr.append(arrList[line][char])
        arr.append(innerArr)

    words = arrList[10].split(";")
    # print
    for line in arr:
        print(line)
    print(words)

    return [arr, words]


input1 = "++++++++++"+"\n"+"+------+++"+"\n"+"+++-++++++"+"\n"+"+++-++++++"+"\n"+"+++-----++"+"\n"+"+++-++-+++" + \
    "\n"+"++++++-+++"+"\n"+"++++++-+++"+"\n"+"++++++-+++" + \
    "\n"+"++++++++++"+"\n"+"POLAND;LHASA;SPAIN;INDIA"
hrInput = input2Arr(input1)



crosswordPuzzle(hrInput[0], hrInput[1])
