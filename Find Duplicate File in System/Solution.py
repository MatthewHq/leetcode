class Solution:
    def findDuplicate(self, paths):

        # was intially heistant to use len() but turns out its O(1)

        # [[parentID,namestart,nameEnd,contentStart,contentEnd]]
        parents = []
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
                charCounter += 1

            counter += 1
        print(parents)


sol = Solution()

sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)",
                  "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
