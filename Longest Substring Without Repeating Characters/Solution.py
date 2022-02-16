class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #using a set because in python a set is implemented as a has table
        # https://wiki.python.org/moin/TimeComplexity
        mySet=set()
        lenCounter=0
        lenMax=0
        for ch in s:
            if ch not in mySet:
                mySet.add(ch)
                lenCounter+=1
            else:
                lenCounter=0
                mySet.clear()
                mySet.add(ch)
                lenCounter+=1
            if lenCounter>lenMax:
                lenMax=lenCounter
        return lenMax


sol = Solution()
# str="abacdefghic"
str="dvdf"

print(sol.lengthOfLongestSubstring(str))