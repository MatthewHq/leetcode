class Solution:
    def generate(self, numRows: int):
        dynMap=[]
        dynMap.append([1])
        if numRows==1:
            return dynMap
        dynMap.append([1,1])

        
        for i in range(2,numRows):
            currRow=[]
            currRow.append(1)
            for j in range(i-1):
                currRow.append(dynMap[i-1][j]+dynMap[i-1][j+1])
            currRow.append(1)
            dynMap.append(currRow)
        return dynMap


    

sol = Solution()
print(sol.generate(2))
            
