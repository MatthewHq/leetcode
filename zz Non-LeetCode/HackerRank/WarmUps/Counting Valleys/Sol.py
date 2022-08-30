def countingValleys(steps, path):
    # Write your code here
    underSea=0
    height=0
    vals=0
    for i in range(len(path)):
        if path[i]=='U':
            height+=1
            if height==0 and underSea>=1:
                vals+=1
                underSea=0
        else: #D
            height-=1
        if height<=0:
            underSea+=1
    return vals
        





path="DDUUDDUDUUUD"
print(countingValleys(None,path))