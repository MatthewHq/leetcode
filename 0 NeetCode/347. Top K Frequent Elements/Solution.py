class Solution:
    def topKFrequent(self, nums, k: int):
        top = []
        lowest = None
        countMap = {}
        for num in nums:
            if countMap.get(num) == None:
                countMap[num] = 1
            else:
                countMap[num] += 1
        #print(countMap)
        if k == len(countMap):
            for key in countMap.keys():
                top.append(key)
        else:
            for key in countMap.keys():
                if len(top) < k:
                    top.append(key)
                    lowest = min(top, key=countMap.get)
                elif countMap[lowest] < countMap[key]:
                    top.append(key)
                    lowest = min(top, key=countMap.get)
                    top.remove(lowest)
                #print(top,lowest,min(top, key=countMap.get))
        return top


# 1 3 4  5  8  9  6  7  0
# 11 2 27 68 91 31 25 96 32
# 11 91 27 68



# 0 0 0 0 0   0
# 1 0 0 0 0   0
# 1 0 0 0 0   0
# 1 0 0 0 0   0


sol = Solution()
nums = [1, 1, 1, 2, 2, 3]
k = 2
#nums=[3,0,1,0]
#k=1

nums=[5,2,5,3,5,3,1,1,3]
k=2
print(sol.topKFrequent(nums, k))
