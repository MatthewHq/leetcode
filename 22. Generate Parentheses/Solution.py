class Solution:
    result=[]
    trackerLimits = []
    trackers = []
    # size
    # currIndex

    def addTo(self, index):
        if index == self.size-1:
                self.result.append(self.genAsText())
                # print(self.genAsText())
        # print("index", index)
        # print("lims", self.trackerLimits)
        # print("track", self.trackers)
        if self.trackers[index] == self.trackerLimits[index]:
            if index != 0:
                self.addTo(index-1)
                for i in range(index, self.size):
                    # print("-------REsetting", i)
                    self.trackers[i] = self.trackers[i-1]+1
                    # print("lims", self.trackerLimits)
                    # print("track", self.trackers)

        else:
            
                # print("lims", self.trackerLimits)
                # print("track", self.trackers)
            self.trackers[index] += 1
        

    def genAsText(self):
        text = ""
        trackerIndex = 0
        # print("===")
        # print(self.trackers)
        for i in range(self.size*2):
            # if trackerIndex <= self.size-1: #DEBUG
            if trackerIndex <= self.size-1 and i == self.trackers[trackerIndex]:
                # print(i,self.trackers[trackerIndex])
                trackerIndex += 1
                text += "("
                # print(text)
            else:
                text += ")"
        return text

    def generateParenthesis(self, n):
        self.result=[]
        # small note, there is a way to make this with dynamic programming for even faster performance
        self.size = n
        for i in range(n):
            self.trackerLimits.append(i*2)
            self.trackers.append(i)

        # print(self.trackerLimits)
        # print(self.trackers)

        # curr will target a specific slot in the trackers array and max it out, starting from the far end
        # self.currIndex = n-1
        while self.trackerLimits != self.trackers:
            self.addTo(self.size-1)
            # if self.trackers[self.currIndex] < self.trackerLimits[self.currIndex]:
            #     print(self.genAsText())
            #     self.trackers[self.currIndex] += 1
            #     if self.currIndex!=self.size-1:
            #         self.currIndex+=1
            # elif self.trackers[self.currIndex] == self.trackerLimits[self.currIndex]:
            #     resetIndex = self.currIndex
            #     if self.trackers[self.currIndex-1] != self.trackerLimits[self.currIndex-1]:
            #         if self.currIndex > 0:
            #             self.currIndex -= 1
            #             resetIndex -= 1
            #     else:
            #         self.currIndex+=1
            #         resetIndex+=1
            #     while resetIndex != self.size:
            #             print("RESET",  resetIndex)
            #             self.trackers[resetIndex] = self.trackers[resetIndex-1]+1
            #             resetIndex += 1

        self.result.append(self.genAsText())
        # print(self.genAsText())
        # print(self.trackerLimits)
        # print(self.trackers)
        return self.result



import time
times={}
for x in range(10):
    for i in range(10,13):
        start_time = time.time()

        sol = Solution()
        sol.generateParenthesis(i)
        if times.get(i)==None:
            times[i]=time.time() - start_time
        else:
            times[i]+=time.time() - start_time
        # print("--- %s seconds ---" % (time.time() - start_time) + str(i))

for i in times.keys():
    print(i,times[i])
