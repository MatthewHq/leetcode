class Solution:
    def countBits(self, n: int):
        base=[0,1]
        if n==0:
            return [0]
        # if base==1:
        #     return base
        lastBracket=0
        bracketCheck=2

        
        for i in range(2,n+1):
            if i >=bracketCheck:
                base.append(1)
                lastBracket=bracketCheck
                bracketCheck*=2
            else:
                base.append(base[i-lastBracket]+1)
        
        return base
                

sol=Solution()



ans=sol.countBits(0)
print(ans,len(ans))

# for i in range(16):
#     print(i,ans[i])

