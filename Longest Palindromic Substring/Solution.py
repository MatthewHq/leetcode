from re import S

class Solution:
    def longestPalindrome(self, s: str) -> str:

        longestStart,longestEnd,longest=0,0,0
        length=len(s)
        dp=[[0 for i in range(length)] for j in range(length)] 
        for i in range(length):
            dp[i][i]=1
        
        for round in range(1,length):
            for start in range(length-round):
                end=start+round
                currLen=end-start+1
                valid=0
                if(s[start]==s[end]):
                    # will be valid if it is either shorter than 2
                    # or if it is longer than 2 and middle substring is not invalid
                    if(not (currLen>2 and dp[start+1][end-1]!=1)):
                        valid=1
                        if longest<currLen:
                            longest=currLen
                            longestStart=start
                            longestEnd=end
                        dp[start][end]=valid
        return s[longestStart:longestEnd+1]
                
                


sol=Solution()
print(sol.longestPalindrome("aaa"))
