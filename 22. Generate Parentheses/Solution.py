class Solution:
    trackerLimits = []
    trackers = []
    # size
    # currIndex

    def genAsText(self):
        text = ""
        trackerIndex = 0
        for i in range(self.size*2):
            if trackerIndex <= self.size-1 and i == self.trackers[trackerIndex]:
                trackerIndex += 1
                text += "("
            else:
                text += ")"
        return text

    def generateParenthesis(self, n):
        # small note, there is a way to make this with dynamic programming for even faster performance
        self.size = n
        for i in range(n):
            self.trackerLimits.append(i*2)
            self.trackers.append(i)

        print(self.trackerLimits)
        print(self.trackers)

        # curr will target a specific slot in the trackers array and max it out, starting from the far end
        self.currIndex = n-1
        while self.trackerLimits != self.trackers:
            if self.trackers[self.currIndex] < self.trackerLimits[self.currIndex]:
                print(self.genAsText())
                self.trackers[self.currIndex] += 1
                if self.currIndex!=self.size-1:
                    self.currIndex+=1
            elif self.trackers[self.currIndex] == self.trackerLimits[self.currIndex]:
                resetIndex = self.currIndex
                if self.trackers[self.currIndex-1] != self.trackerLimits[self.currIndex-1]:
                    if self.currIndex > 0:
                        self.currIndex -= 1
                        resetIndex -= 1
                else:
                    self.currIndex+=1
                    resetIndex+=1
                while resetIndex != self.size:
                        print("RESET",  resetIndex)
                        self.trackers[resetIndex] = self.trackers[resetIndex-1]+1
                        resetIndex += 1
            print("lims", self.trackerLimits)
            print("track", self.trackers)

        print(self.genAsText())
        print(self.trackerLimits)
        print(self.trackers)


sol = Solution()
sol.generateParenthesis(4)
