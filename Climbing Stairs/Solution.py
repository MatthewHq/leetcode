class Solution:
    def climbStairs(self, n: int) -> int:
        stepMap=[]
        stepMap.append(1)
        stepMap.append(2)

        if n==1:
            return 1
        elif n==2:
            return 2
        else:
            for i in range(2,n):
                stepMap.append(stepMap[i-1]+stepMap[i-2])
            return stepMap[n-1]



sol = Solution()
print(sol.climbStairs(4))
