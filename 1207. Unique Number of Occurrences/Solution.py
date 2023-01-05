class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occ = {}
        for i in arr:
            if occ.get(i)==None:
                occ[i]=1
            else:
                occ[i]+=1

        conflicts={}
        for i in occ.values():
            if conflicts.get(i)!=None:
                return False
            else:
                conflicts[i]=True

        return True