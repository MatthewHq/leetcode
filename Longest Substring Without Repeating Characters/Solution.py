class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDc={}
        lenCounter=0
        lenMax=0
        for i in range(len(s)):
            if myDc.get(s[i])==None:
                myDc[s[i]]=i
                lenCounter+=1
            else:
                lenCounter=0
                print(i," | ", myDc.get(s[i])," | ",s[i]," | ",i-myDc.get(s[i])-1)
                lenCounter=i-myDc.get(s[i])-1
                print(lenCounter)
                myDc[s[i]]=i
                lenCounter+=1
            if lenCounter>lenMax:
                lenMax=lenCounter
        return lenMax


sol = Solution()
# str="abacdefghic"
str="dvdf"
str="abba"
print(sol.lengthOfLongestSubstring(str))