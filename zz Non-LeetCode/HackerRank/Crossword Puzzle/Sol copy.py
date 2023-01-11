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
class WordSlot():
    def __init__(self,id,pairs,type):
        self.id=id
        self.type=type
        self.connections=[]
        self.start=pairs[0]
        self.end=pairs[1]
        self.length=None
    def __repr__(self):
        return "({},{} | {})".format(self.start,self.end,self.connections)
        

class Connection():
    def __init__(self,ownerId,connectedTo,location):
        self.ownerId=ownerId #wordSlot ID
        self.connectedTo=connectedTo #id of who the owner is connected to
        self.location=location
        self.ownerSlot=None #at which location in the word is the junction
        self.connectedSlot=None #at which location in the word is the junction
    def __repr__(self):
        return "({}<->{})".format(self.ownerId,self.connectedTo)

class End():
    def __init__(self,type,coords):
        self.type = type
        self.coords = coords

    def __str__(self):
        return "{} @ {}".format(self.type,self.coords)

    def __repr__(self):
        return "{} @{}".format(self.type,self.coords)

def crosswordPuzzle(crossword, words):
    idTracker=[0]
    visited = {}
    for x in range(10):
        for y in range(10):
            visited[(x, y)] = True
    print(visited)

    ends = []
    while len(visited) > 0:
        coordTuple = visited.popitem()[0]
        # print("popped", coordTuple)
        recursiveExplore(coordTuple, crossword, visited,ends)
        
    print(ends)
    print(visited)

    horizontal={}
    vertical={}

    for end in ends:
        if end.type%2==0:
            if vertical.get(end.coords[1])==None:
                vertical[end.coords[1]]=[end.coords]
            else:
                vertical[end.coords[1]].append(end.coords)
        else:
            if horizontal.get(end.coords[0])==None:
                horizontal[end.coords[0]]=[end.coords]
            else:
                 horizontal[end.coords[0]].append(end.coords)

    
    print("HORIZONTAL",horizontal)
    print("VERTICAL",vertical)
    
    horizontalSlots={}
    verticalSlots={}

    getPairs(horizontal,1,horizontalSlots,idTracker)
    
    print("HORIZONTAL")
    print("id tracker",idTracker)
    

    getPairs(vertical,0,verticalSlots,idTracker)
    
    print("VERTICAL")
    print("id tracker",idTracker)

    print(horizontalSlots,"\n",verticalSlots)



    
    for hpair in horizontalSlots.values():
        for vpair in verticalSlots.values():
            intersects(hpair,vpair)
    
    print(horizontalSlots,"\n",verticalSlots)


def intersects(hSlot,vSlot):
    intersects=[]
    h=(hSlot.start,hSlot.end)
    v=(vSlot.start,vSlot.end)
    # print(h[0][0],v[0][0],v[1][0],"AND",v[0][1],h[0][1],h[1][1])
    if h[0][0]>= v[0][0] and h[0][0]<=v[1][0] and v[0][1]>=h[0][1] and v[0][1]<=h[1][1]:
        intersects.append((h[0][0],v[0][1]))
        hSlot.connections.append(Connection(hSlot.id,vSlot.id,(h[0][0],v[0][1])))
        vSlot.connections.append(Connection(vSlot.id,hSlot.id,(h[0][0],v[0][1])))
        
    


def getPairs(dict,lam,slotBank,idTracker):
    print("dictprint",dict)
    print("dictkeys",dict.keys())
    # pairs=[]
    for lineArrs in dict.values():
        pair=[]
        # print("lineArrs",lineArrs)
        if len(lineArrs)>2:
            lineArrs.sort(key=lambda x:x[1])
            print(lineArrs)
            
            while len(lineArrs)>2:
                pair.append(lineArrs.pop(0))
                if len(pair)==2:
                    slotBank[idTracker[0]]=WordSlot(idTracker[0],pair.copy(),lam)
                    idTracker[0]+=1
                    # pairs.append(pair.copy())
                    pair.clear()
            slotBank[idTracker[0]]=WordSlot(idTracker[0],lineArrs,lam)
            idTracker[0]+=1
            # pairs.append(lineArrs)
            # print("postPOP",lineArrs)
            # print("postPOP",dict)
        else:
            lineArrs.sort(key=lambda x:x[lam])
            slotBank[idTracker[0]]=WordSlot(idTracker[0],lineArrs,lam)
            idTracker[0]+=1
            # pairs.append(lineArrs)
    # return pairs
        


def recursiveExplore(coords, crossword, visited,ends):
    if visited.get(coords) != None:
        del visited[coords]
    # print("RECURSING ON",coords)
    if crossword[coords[0]][coords[1]] == "-":
        for i in range(4):
            peekInto = move(coords, i)
            
            if bound(peekInto) and crossword[peekInto[0]][peekInto[1]] == "-":
                oppositePeek=move(coords,(i+2)%4)
                if not bound(oppositePeek) or crossword[oppositePeek[0]][oppositePeek[1]] != "-":
                    ends.append(End((i+2)%4,coords))
                if visited.get(peekInto) != None:
                    recursiveExplore(peekInto, crossword, visited, ends)                
    else:
        return None

# 0 1 2 3 = down0 right1 up2 left3

def bounds(coords,min,max):
    if coords[0]<min or coords[1]<min or coords[0]>max or coords[1]>max:
        return False
    return True

def bound(coords):
    return bounds(coords,0,9)


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

input2="++++++++++"+"\n"+"+-----+---"+"\n"+"+++-++++++ "+"\n"+"+++-++++++ "+"\n"+"+++-----++ "+"\n"+"+++-++-+++ "+"\n"+"++++++-+++ "+"\n"+"++++++-+++ "+"\n"+"++++++-+++ "+"\n"+"++++++++++"+"\n"+"POLAND;LHASA;SPAIN;INDIA"
input3="++++++++++"+"\n"+"+-----+--+"+"\n"+"+++-++++++"+"\n"+"+++-++++++"+"\n"+"+++-----++"+"\n"+"+++-++-+++"+"\n"+"++++++-+++"+"\n"+"++++++-+++"+"\n"+"+-++++-+++"+"\n"+"++++++++++"+"\n"+"POLAND;LHASA;SPAIN;INDIA"
hrInput = input2Arr(input3)

crosswordPuzzle(hrInput[0], hrInput[1])
