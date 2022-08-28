class Solution:
    def minDifficulty(self, jobDifficulty, d):
        srResults=self.splitRange(0, len(jobDifficulty), jobDifficulty)
        print(srResults)
        firstMin=self.getFirstMin(srResults)
        print(firstMin)
    def splitRange(self, start, end, array):
        splitVals = []
        for i in range(end-start-1):
            x = i+start+1
            #note instead of max() there can be a more memory intensive way to save on processing to achieve slightly better results, though it would be more complicated
            splitVals.append([max(array[start:x]), max(array[x:end])])
            print(array[start:x], array[x:end])
        return splitVals

    def getFirstMin(self,srResults):
        minIndex=0
        minVal=None
        for i in range(len(srResults)):
            added=sum(srResults[i])
            if minVal==None or added<minVal:
                minVal=added
                minIndex=i
        return minIndex




sol = Solution()


diffs = [1, 2, 3, 4, 5, 6]
diffs = [1,5,2,4,8,1,7]
diffs = [10,5,2,4,8,1,7]
sol.minDifficulty(diffs, 2)
