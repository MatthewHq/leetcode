class Solution:
    def findDuplicate(self, paths):

        # was intially heistant to use len() but turns out its O(1)

        counter = 0
        while(counter < len(paths)):
            charCounter = 0
            while(charCounter < len(paths[counter])):
                print(paths[counter][charCounter])
                charCounter += 1
            counter += 1


sol = Solution()

sol.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"])
