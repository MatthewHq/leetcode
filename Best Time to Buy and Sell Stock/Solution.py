class Solution:
    def maxProfit(self, prices) -> int:
        leftSelector = prices[0]
        leftExplorer = prices[0]
        rightExplorer = prices[len(prices)-1]
        rightSelector = prices[len(prices)-1]

        maxProfit = 0

        while(leftExplorer != rightSelector and rightExplorer != leftSelector):
            leftCheck = leftExplorer-leftSelector
            rightCheck = rightSelector-rightExplorer
            endCheck = rightSelector-leftSelector

            if (leftCheck > maxProfit):
                maxProfit = leftCheck



sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 1, 100, 6, 4]))
