class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDc = {}
        lenCounter = 0
        lenMax = 0
        lastestValid = 0
        for i in range(len(s)):
            if myDc.get(s[i]) == None:
                myDc[s[i]] = i
                lenCounter += 1
            else:
                lenCounter = 0
                lastestValid=myDc.get(s[i]) if myDc.get(s[i])>lastestValid else lastestValid
                lenCounter = i-lastestValid-1
                myDc[s[i]] = i
                lenCounter += 1
            if lenCounter > lenMax:
                lenMax = lenCounter
        return lenMax


sol = Solution()
str="abacdefghic"
str = "dvdf"
str = "abba"
print(sol.lengthOfLongestSubstring(str))
