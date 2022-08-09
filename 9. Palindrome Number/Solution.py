from numpy import place


class Solution:
    def isPalindrome(self, x: int) -> bool:
        orderedPlaces=self.decimalPlaces(x)
        print(orderedPlaces)
        if x<0:
            return False

        for i in range(len(orderedPlaces)-1):
            orderedPlaces[i]=orderedPlaces[i]-orderedPlaces[i+1]*10
        print(orderedPlaces)

        pal=True
        for i in range(len(orderedPlaces)):
            size=len(orderedPlaces)
            j=size-1-i

            if j<=i:
                break
            
            if orderedPlaces[i]!=orderedPlaces[j]:
                pal=False
        return pal

    def decimalPlaces(self,x):
        places=[]
        places.append(x)
        while (x>=10)or(x<=-10) :
            x=x//10
            places.append(x)
            print(x)
        return places




sol = Solution()
print(sol.isPalindrome(11))
# print(sol.testing)
