from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=s.lower()
        #print(r)
        finalS=""
        for c in r:
            if (ord(c)>=97 and ord(c)<=122)or ord(c)>=48 and ord(c)<=57:
                finalS+=c
        print(finalS)
        amount=len(finalS)//2
        for i in range(amount):
            if finalS[i]!=finalS[len(finalS)-1-i]:
                return False
        return True

sol = Solution()
s=""
s ="A man, a plan, a canal: Panama"
# s="0P"
print(sol.isPalindrome(s))

