class Solution:
    def generateParenthesis(self, n):
        #small note, there is a way to make this with dynamic programming for even faster performance
        trackerLimits=[]
        trackers=[]
        for i in range(n):
            trackerLimits.append(i*2)
            trackers.append(i)

        print(trackerLimits)
        print(trackers)

        #curr will target a specific slot in the trackers array and max it out, starting from the far end
        curr=n-1
        while trackerLimits!=trackers:
            if trackers[curr]!=trackerLimits[curr]:
                


sol = Solution()
sol.generateParenthesis(4)



