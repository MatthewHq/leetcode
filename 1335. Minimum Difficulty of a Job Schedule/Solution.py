class Solution:
    def minDifficulty(self, jobDifficulty, d):
        if d > len(jobDifficulty):
            return -1
        print(jobDifficulty)
        cuts=[]
        nextRange=[]
        for i in range(d-1):
            nextRange=self.makeRanges(cuts,jobDifficulty)
            print("nextRange",nextRange)
            srResults=self.splitRange(nextRange, jobDifficulty)
            print("srResults",srResults)
            firstMin=self.getFirstMin(srResults)
            print("firstMin",firstMin)
            cuts.append(firstMin)
        # firstRange=[[0, len(jobDifficulty)]]
        # srResults=self.splitRange(firstRange, jobDifficulty)
        # firstMin=self.getFirstMin(srResults)
        

        
        # print(srResults)
        
        # print(firstMin)
        # cuts.append(2)
        # cuts.append(firstMin)
        # cuts.append(5)
        
        # print(self.makeRanges(cuts,jobDifficulty))\
        cuts.sort()
        print(cuts)
        return self.getRangeSums(cuts,jobDifficulty)


        

    def splitRange(self,rangeList, array):
        #print("====SPLITTING RANGES====",rangeList)
        splitVals = []
        for rangePair in rangeList:
            print("==spliting==",rangePair)
            start=rangePair[0]
            end=rangePair[1]+1
            for i in range(end-start-1):
                x = i+start+1
                #note instead of max() there can be a more memory intensive way to save on processing to achieve slightly better results, though it would be more complicated
                # print(array[start:x],array[x:end],start,end,x)
                splitVals.append([max(array[start:x]), max(array[x:end]),x-1])
                #print("range Made",array[start:x], array[x:end])
        return splitVals

    def getFirstMin(self,srResults):
        minIndex=0
        addeds=[] #DEBUG
        minVal=None
        for i in range(len(srResults)):
            added=srResults[i][0]+srResults[i][1]
            addeds.append(added) #DEBUG
            if minVal==None or added<minVal:
                minVal=added
                minIndex=i
        print("ALL ADDEEDSSS",addeds)#DEBUG
        return srResults[minIndex][2]

    def getRangeSums(self,cuts,arr):
        cuts.sort()
        result=0
        start=0
        for cut in cuts:
            rg=arr[start:cut+1]
            #print("len",len(rg),rg)
            if len(rg)>1:
                #print("adding",max(rg))
                result+=max(rg)
            else:
                #print("adding",arr[cut])
                result+=arr[cut]
            start=cut+1
        lastRg=arr[start:len(arr)]
        #print("len",len(rg),rg)
        if len(lastRg)>1:
                #print("adding",max(lastRg))
                result+=max(lastRg)
        else:
                #print("adding",arr[len(arr)-1])
                result+=arr[len(arr)-1]
        return result


        
    
    def makeRanges(self,cuts,arr):
        cuts.sort()
        start=0
        rangeList=[]
        for i in cuts:
            end=i
            rangeList.append([start,end])
            start=end+1
        rangeList.append([start,len(arr)-1])
        return rangeList
            


        




sol = Solution()


jobDifficulty = [1, 2, 3, 4, 5, 6]
jobDifficulty = [1,5,2,4,8,1,7]
# jobDifficulty = [10,5,2,4,8,1,7]
# jobDifficulty = [6,5,4,3,2,1]
# jobDifficulty = [1,1]
jobDifficulty=[186,398,479,206,885,423,805,112,925,656,16,932,740,292,671,360]
print(sol.minDifficulty(jobDifficulty, 4))
