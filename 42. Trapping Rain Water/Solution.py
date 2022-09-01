class Solution:
    def trap(self, height):
        # double array of [[start,end]]
        cutsQ = [[0, len(height)-1]]
        wholeSet=cutsQ.pop()
        largeSet=self.get2Largest(wholeSet, height)
        
        print(largeSet)
        self.produceCuts(largeSet,wholeSet,height,cutsQ)

    def produceCuts(self, largeSet, wholeSet, arr, cutsQueue):
        pass

    # return 2 largest indices in one double array
    def get2Largest(self, wholeSet, arr):
        large = [[0, None], [0, None]]
        for i in range(wholeSet[1]-wholeSet[0]):
            if arr[i] >= large[0][0]:
                large[1] = large[0]
                large[0] = [arr[i], i]
            elif arr[i] >= large[1][0]:
                large[1] = [arr[i], i]
        return large


sol = Solution()


height = [1, 0, 6, 0, 1, 0, 5, 0, 1, 1, 2]
print(sol.trap(height))
