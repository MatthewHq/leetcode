from ssl import ALERT_DESCRIPTION_ILLEGAL_PARAMETER


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print("a")
        aMap={}
        for c in s:
            if c not in aMap.keys():
                aMap[c]=1
            else:
                aMap[c]+=1
        print(aMap)


        
        # for c in s:
        #     if aMap[.get(c)]==None:
        #         aMap[c]=1
        #     else:
        #         aMap[c]+=1
            


sol =Solution()

sol.isAnagram("banana","b")