

class Solution:
    def findDuplicate(self, paths):
        duplicates = []
        # was intially heistant to use len() but turns out its O(1)

        # [[parentID,namestart,nameEnd,contentStart,contentEnd]]
        parents = []
        sortedContents = {}
        counter = 0
        while(counter < len(paths)):
            nameStart, nameEnd, contentStart, contentEnd, lazyHash = 0, 0, 0, 0, 0
            parentID = counter
            charCounter = 0
            parentFlag = True
            inContent = 0
            while(charCounter < len(paths[counter])):
                # print(counter, paths[counter][charCounter])
                if paths[counter][charCounter] == ' ':
                    if parentFlag:
                        parentFlag = False
                        parents.append(charCounter-1)
                    # else:
                    nameStart = charCounter+1
                elif paths[counter][charCounter] == '(':
                    nameEnd = charCounter-1
                    contentStart = charCounter+1
                    inContent = 1
                elif paths[counter][charCounter] == ')':
                    inContent = 0
                    contentEnd = charCounter-1
                    contentSize = contentEnd-contentStart+1
                    if sortedContents.get(contentSize) == None:
                        sortedContents[contentSize] = {}
                    if sortedContents.get(contentSize).get(lazyHash) == None:
                        sortedContents.get(contentSize)[lazyHash] = []

                    sortedContents[contentSize][lazyHash].append(
                        [parentID, nameStart, nameEnd, contentStart, contentEnd])
                    lazyHash = 0

                if inContent == 1:
                    inContent = 2
                elif inContent == 2:
                    lazyHash += ord(paths[counter][charCounter])
                charCounter += 1

            counter += 1
        print(parents)
        # print(sortedContents.keys())

        print(sortedContents)
        # for size in sortedContents.keys():
        #     print("testSize",size)

        for size in sortedContents.keys():
            print("size",size)
            for hashBracket in sortedContents.get(size).values():
                print("bracket",hashBracket)
                while(len(hashBracket) > 1):
                    # print(hashBracket.pop(0),"popping")
                    inView = hashBracket.pop(0)
                    pops = []
                    compareIndex = 0
                    for comparedTo in hashBracket:
                        for i in range(size):
                            # print(paths[comparedTo[0]][comparedTo[3]+i])
                            # print(paths[inView[0]][inView[3]+i])
                            if paths[inView[0]][inView[3]+i] != paths[comparedTo[0]][comparedTo[3]+i]:
                                break
                            if i == size-1:
                                pops.append(compareIndex)
                        compareIndex += 1
                    print("POPS", pops)

                    if len(pops) != 0:
                        dupeBatch = []
                        popShifter = 0
                        for pop in pops:
                            justPopped = hashBracket.pop(pop-popShifter)
                            dupeBatch.append(self.dataPrinter(
                                parents, paths, justPopped))
                            # print(self.dataPrinter(parents, paths, justPopped),
                            #       self.contentPrinter(paths, justPopped))
                            popShifter += 1
                        dupeBatch.append(self.dataPrinter(
                            parents, paths, inView))
                        # print(self.dataPrinter(parents, paths, inView),
                        #       self.contentPrinter(paths, inView))
                        duplicates.append(dupeBatch)
        return duplicates

    def dataPrinter(self, parents, paths, data):
        file = ""
        for i in range(parents[data[0]]+1):
            file += paths[data[0]][i]

        file += '/'

        for i in range(data[1], data[2]+1):
            file += paths[data[0]][i]
        # for i in range(data[1],data[2]):

        return file

    def contentPrinter(self, paths, data):
        content = ""

        for i in range(data[3], data[4]+1):
            content += paths[data[0]][i]

        return content


sol = Solution()

# print(sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
#                   "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(egfh) 5.txt(fgeh) 6.txt(egfh)"]))
# sol.findDuplicate(["root/a 1.txt(efgh) 2.txt(abcd)",
#                   "root/c 3.txt(abcd)", "root/c/d 4.txt(efhg)", "root 4.txt(efgh)", "root/r 2.txt(efgh)"])


print(sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efsfgh) 3.txt(efsfgh)",
      "root/c 3.txt(abdfcd)", "root/c/d 4.txt(efggdfh)"]))
