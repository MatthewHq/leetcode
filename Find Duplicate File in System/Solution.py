from numpy import size


class Solution:
    def findDuplicate(self, paths):

        # was intially heistant to use len() but turns out its O(1)

        # [[parentID,namestart,nameEnd,contentStart,contentEnd]]
        parents = []
        bySizeContents = {}
        counter = 0
        while(counter < len(paths)):
            nameStart, nameEnd, contentStart, contentEnd = 0, 0, 0, 0
            parentID = counter
            charCounter = 0
            parentFlag = False
            while(charCounter < len(paths[counter])):
                print(counter, paths[counter][charCounter])
                if paths[counter][charCounter] == ' ':
                    if not parentFlag:
                        parentFlag = True
                        parents.append(charCounter-1)
                    else:
                        nameStart = charCounter+1
                elif paths[counter][charCounter] == '(':
                    nameEnd = charCounter-1
                    contentStart = charCounter+1
                elif paths[counter][charCounter] == ')':
                    contentEnd = charCounter-1
                    contentSize = contentEnd-contentStart+1
                    if bySizeContents.get(size) == None:
                        bySizeContents[size] = []
                    bySizeContents[size].append(
                        [parentID, nameStart, nameEnd, contentStart, contentEnd])
                charCounter += 1

            counter += 1
        print(parents)
        print(bySizeContents)


sol = Solution()

sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                  "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
