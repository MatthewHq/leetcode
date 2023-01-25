class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount={}
        if len(t)!=len(s):
            return False
        for c in s:
            if charCount.get(c)==None:
                charCount[c]=1
            else:
                charCount[c]+=1

        for c in t:
            if charCount.get(c)==None:
                return False
            else:
                charCount[c]-=1
                if charCount[c]<0:
                    return False

        return True
        


s="anagram"
t="nagaram"
sol=Solution()
print(sol.isAnagram(s,t))