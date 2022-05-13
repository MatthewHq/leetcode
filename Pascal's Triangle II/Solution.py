class Solution:
    def generate(self, rowIndex):
        dynMap=[]
        dynMap.append([1])
        if rowIndex==0:
            return dynMap[0]
        dynMap.append([1,1])

        
        for i in range(2,rowIndex+1):
            currRow=[]
            currRow.append(1)
            for j in range(i-1):
                currRow.append(dynMap[i-1][j]+dynMap[i-1][j+1])
            currRow.append(1)
            dynMap.append(currRow)
        return dynMap[rowIndex]


    

sol = Solution()
print(sol.generate(0))
            
