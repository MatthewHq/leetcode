

def isValid(s):
    # Write your code here
    dt = {}

    for c in s:
        if dt.get(c) == None:
            dt[c] = 1
        else:
            dt[c] += 1


    maxFlag=0

    freqCount={}

    for val in dt.values():
        if freqCount.get(val) == None:
            freqCount[val] = 1
        else:
            freqCount[val] += 1

    print(dt)
    print(freqCount)
    if freqCount.__len__() >2:
        return 'NO'
    
    

    if freqCount.__len__() ==2:
        freqList=list(freqCount.keys())
        if(abs(freqList[0]-freqList[1]))!=1:
            return 'NO'

        print(type(freqList))
        maxKey=max(freqList)
        print(freqCount[maxKey])
        if(freqCount[maxKey]>1):
            return 'NO'

    return'YES'


    # if size(freqCount)



print(isValid("hhhhiiiiooooo"))
