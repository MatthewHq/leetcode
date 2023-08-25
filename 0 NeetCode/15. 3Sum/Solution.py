from typing import List
class Solution:
    def calcNegativeHash(self,nums):
        negHash={}
        for i in range(len(nums)):
            tar=nums[i]*-1
            if negHash.get(tar)==None:
                negHash[tar]=[i]
            else:
                negHash[tar].append(i)
        return negHash

    def reduceNums(self,nums):
        newNums=[]
        reduceCache={}
        for i in nums:
            if reduceCache.get(i)!=None:
                if reduceCache[i]<3:
                    reduceCache[i]+=1
                    newNums.append(i)
            else:
                reduceCache[i]=1
                newNums.append(i)
        return newNums

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # print(nums)
        nums=self.reduceNums(nums)
        # print(nums)
        negativeHash=self.calcNegativeHash(nums)
        completeSols=[]
        setCheck={}
        debugByIndex=[]

        

        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)-1):
                sum2=nums[i]+nums[j]
                if negativeHash.get(sum2)!=None:
                    sols=negativeHash.get(sum2)
                    for k in range(len(sols)):
                        if sols[k]>j:
                            debugByIndex.append([i,j,sols[k]])
                            sort=sorted([nums[i],nums[j],nums[sols[k]]])
                            joinedSTR='^'.join(str(x)for x in sort)
                            if setCheck.get(joinedSTR)==None:
                                completeSols.append(sort)
                                setCheck[joinedSTR]=True
                                # print(setCheck)


                            
                # print([i,j])
        return completeSols

sol = Solution()
nums=[-1,0,1,2,-1,-4]
nums=[0,0,0,0,0,0]
print(sol.threeSum(nums))
