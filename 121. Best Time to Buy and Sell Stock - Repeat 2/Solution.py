class Solution:
    def maxProfit(self, prices) -> int:
        prof=0
        if len(prices) < 2:
            return 0
        small, big = None, None
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                if small == None:
                    small = prices[i]
                if big == None:
                    big = prices[i+1]
                elif prices[i+1] > big:
                    big = prices[i+1]
            else:
                if small != None and prices[i+1] < small:
                    small = prices[i+1]
                    big=small
            if small != None and big != None and big-small>prof:
                prof=big-small
        return prof


prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))
