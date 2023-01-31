class Solution:
    def groupAnagrams(self, strs):
        groups={}
        for anaStr in strs:
            asKey=self.strToKey(anaStr)
            if groups.get(asKey)==None:
                groups[asKey]=[anaStr]
            else:
                groups[asKey].append(anaStr)
        groupedAnas=[]
        for group in groups.values():
            groupedAnas.append(group)
        return groupedAnas

    def strToKey(self,cStr):
        arr=[0 for x in range(26)]
        for c in cStr:
            arr[ord(c)-97]+=1
        keyStr=""
        for i in arr:
            keyStr+=str(i)
            keyStr+='|'
        return keyStr
        

strs = ["bdddddddddd","bbbbbbbbbbc"]

sol = Solution()
print(sol.groupAnagrams(strs))




#eat
#
#  {1,2,3,4,5,6.....K}
#  [a,b,c,d,e]
#