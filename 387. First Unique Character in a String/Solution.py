class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars={}
        charOrder=[]
        counter=0
        for i in s:
            if chars.get(i):
                chars[i]+=1
            else:
                chars[i]=1
                charOrder.append([i,counter])
            counter+=1

        for i in charOrder:
            if chars[i[0]]==1:
                return i[1]
        return -1

sol=Solution()

print(sol.firstUniqChar("leetcode"))