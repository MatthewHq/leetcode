class Solution:
    def maxProfit(self, prices) -> int:

        leftSelector = 0
        leftExplorer = 1
        rightExplorer = len(prices)-2
        rightSelector = len(prices)-1

        leftMax = 0
        rightMax = 0
        maxProfit = 0
        cycle = -1

        if len(prices) == 2:
            if prices[1] > prices[0]:
                maxProfit = prices[1]-prices[0]
        elif len(prices) > 2:
            # while(leftExplorer != rightSelector and rightExplorer != leftSelector):
            while(leftExplorer <= rightExplorer):
                leftCheck = prices[leftExplorer]-prices[leftSelector]
                rightCheck = prices[rightSelector]-prices[rightExplorer]
                endCheck = prices[rightSelector]-prices[leftSelector]
                # print(leftSelector, leftExplorer,
                #       rightExplorer, rightSelector, "-0--")
                if cycle != -1:
                    if cycle == 0:
                        if prices[leftExplorer] < prices[leftSelector]:
                            leftSelector = leftExplorer
                        leftExplorer += 1
                        cycle = 1
                    elif cycle == 1:
                        if prices[rightExplorer] > prices[rightSelector]:
                            rightSelector = rightExplorer
                        rightExplorer -= 1
                        cycle = 2
                    elif cycle == 2:
                        if prices[leftExplorer] < prices[leftSelector]:
                            leftSelector = leftExplorer
                        cycle = 3
                    elif cycle == 3:
                        cycle = 0
                        if prices[rightExplorer] > prices[rightSelector]:
                            rightSelector = rightExplorer

                else:
                    cycle = 0

                # print(leftSelector, leftExplorer,
                #       rightExplorer, rightSelector, "-0--")
                # print(leftCheck, rightCheck, endCheck)

                if (leftCheck > maxProfit):
                    maxProfit = leftCheck
                    leftMax = leftSelector
                    rightMax = leftExplorer
                if(rightCheck > maxProfit):
                    maxProfit = rightCheck
                    leftMax = rightExplorer
                    rightMax = rightSelector
                if(endCheck > maxProfit):
                    maxProfit = endCheck
                    leftMax = leftSelector
                    rightMax = rightSelector
        # print(maxProfit)
        return maxProfit


sol = Solution()
assert sol.maxProfit([200, 400, 100, 0, 300, 50, 200, 0, 200])==300
assert sol.maxProfit([7, 6, 4, 3, 1])==0

assert sol.maxProfit([1, 2, 4])==3
assert sol.maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2
assert sol.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 4
assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
