class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowelChart=[[1,1,1,1,1]]
        for i in range(1,n):
            newRow=[]
            newRow.append(1)
            rollingSum=1
            for j in range(1,5):
                rollingSum+=vowelChart[i-1][j]
                newRow.append(rollingSum)
            vowelChart.append(newRow)
        return sum(vowelChart[n-1])



sol =Solution()
print(sol.countVowelStrings(33))