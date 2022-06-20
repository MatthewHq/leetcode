from re import L


class Solution:
    def maxProfit(self, prices) -> int:
        prof=0
        small=float('inf')
        for i in range(len(prices)):
            if prices[i]<small:
                small=prices[i]
            elif prices[i]-small > prof:
                prof=prices[i]-small
        return prof
            


prices = [7,6,4,3,1]
sol = Solution()
print(sol.maxProfit(prices))