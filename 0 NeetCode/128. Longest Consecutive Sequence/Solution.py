
class Solution:
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        lengths={}
        
        for num in nums:
            lengths[num]=1

        for key in lengths.keys():
            #print("key----")
            if lengths[key]==1:#could probably use a dif structure in a sort of islands approach?
                #print("not 1----")
                val=key+1
                while lengths.get(val)!=None:
                    # print("====\nkey {}-{}  val{}-{}".format(key,lengths[key],val,lengths[val]))
                    lengths[key]=lengths[key]+lengths[val]
                    hold=lengths[val]
                    lengths[val]=0
                    # print("key {}-{}  val{}-{}\n====".format(key,lengths[key],val,lengths[val]))
                    val+=hold
        # print(lengths)
        return max(lengths.values())

        

sol = Solution()
nums = [100,6,7,4,5,200,1,3,2]
nums = [10,9,8,7,6,1,2,3,4,5]
nums = [100,4,200,1,3,2]
print(sol.longestConsecutive(nums))