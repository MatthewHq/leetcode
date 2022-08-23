class Solution:
    def merge(self, intervals):
        tagger = {}  # 0=Start 1=End, -1=singles
        bank = []
        brackets = []

        for i in intervals:
            if i[0] == i[1]:
                if tagger.get(i[0]) == None:
                    tagger[i[0]] = {}
                    bank.append(i[0])
                if tagger[i[0]].get(-1) == None:
                    tagger[i[0]][-1] = 1
                else:
                    tagger[i[0]][-1] += 1
            else:
                if tagger.get(i[0]) == None:
                    tagger[i[0]] = {}
                    bank.append(i[0])
                if tagger[i[0]].get(0) == None:
                    tagger[i[0]][0] = 1
                else:
                    tagger[i[0]][0] += 1
                if tagger.get(i[1]) == None:
                    tagger[i[1]] = {}
                    bank.append(i[1])
                if tagger[i[1]].get(1) == None:
                    tagger[i[1]][1] = 1
                else:
                    tagger[i[1]][1] += 1

        bank.sort()
        start = None
        end = None
        lastEnd = None
        firstStart = None
        counter = 0
        singleBracketBank = []

        # print(bank, tagger)
        for x in range(len(bank)):
            i = bank[x]
            # print(i, tagger[i])
            if tagger[i].get(-1) and not ((tagger[i].get(0) or tagger[i].get(1))):
                # print(end, start)
                if end or start == None:
                    # print(i,"APPEDNING A")
                    brackets.append([i, i])
            # if not (tagger[i].get(0) and tagger[i].get(1)):  # both
            if tagger[i].get(0):  # start
                if firstStart == None:
                    firstStart = i
                    start = True
                    end = False
                
                
                # print(i-1, lastEnd, counter)
                if (i-1 != lastEnd or counter == 0):
                    #and (firstStart!=None and lastEnd!=None)
                    if end:
                        end = False
                        start = True
                        # for i in singleBracketBank:
                        #     brackets.append(i)
                        # singleBracketBank.clear()
                        brackets.append([firstStart, lastEnd])
                        # print(firstStart,"APPEDNING B")
                        firstStart = i
                else:
                    start = True
                    end = False
                counter += tagger[i][0]
                # print(counter,"ADDED")
            if tagger[i].get(1):  # end
                counter -= tagger[i][1]
                # print(counter,"SUBBED")
                if not tagger[i].get(0):
                    start = False
                    end = True
                    lastEnd = i

                # print("HEY", i)
        if lastEnd!=None:
            brackets.append([firstStart, lastEnd])
        # print(bank)
        return brackets


intervals = [[1, 3], [2, 6], [12, 19], [23, 25], [28, 30],  # [[1, 6], [8, 19], [23, 26], [28, 30], [32, 34]]
             [32, 33], [33, 34], [8, 13], [23, 26], [29, 30]]
# intervals = [[1, 4], [0, 0], [2, 2]]  # [[0, 0], [1, 4]]
# intervals = [[1, 4], [0, 2], [3, 5]]  # [[0, 5]]
# intervals = [[1, 4], [5, 6]]  # [[1, 4], [5, 6]]
# intervals = [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]  # [[5, 5], [2, 4]]
# intervals = [[2, 3], [2, 2], [3, 3], [1, 3],
#              [5, 7], [2, 2], [4, 6]]  # [[1,3],[4,7]]

# intervals = [[1, 3], [0, 2], [2, 3], [4, 6], [
#     4, 5], [5, 5], [0, 2], [3, 3]]  # [[0,3],[4,6]]
intervals=[[1,1],[3,3],[0,0],[0,0],[1,1]]

sol = Solution()
print(sol.merge(intervals))
