import hmac


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts , verticalCuts) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        hMax=self.maxGap(h,horizontalCuts)
        wMax=self.maxGap(w,verticalCuts)

        return (wMax*hMax) % ((10 ** 9) + 7)

    def maxGap(self,x,cuts):
        maxG=cuts[0]
        for i in range(len(cuts)-1):
            if cuts[i+1]-cuts[i]>maxG:
                maxG=cuts[i+1]-cuts[i]

        if x-cuts[len(cuts)-1]>maxG:
            maxG=x-cuts[len(cuts)-1]
        return maxG 


            



h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]


# h = 5
# w = 4
# horizontalCuts = [3,1]
# verticalCuts = [1]

# h = 5
# w = 4
# horizontalCuts = [3]
# verticalCuts = [3]


sol = Solution()
print(sol.maxArea(h,w,horizontalCuts,verticalCuts))




