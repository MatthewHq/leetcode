class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1],reverse=True)
        space=truckSize
        i=0
        maxUnits=0
        while space>0 and i <len(boxTypes):
            perBox=boxTypes[i][1]
            if boxTypes[i][0]>=space:
                maxUnits+=space*perBox
                space=0
            else:
                space-=boxTypes[i][0]
                maxUnits+=boxTypes[i][0]*perBox
            i+=1
        return maxUnits