from typing import List,Optional
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        l=0
        r=m*n-1
        pt=r-(r-l)//2
        
        
        while l<=r:
            curr=self.getMtrx(self.toMtrx(n,pt),matrix)
            # print(curr)
            if target>curr:
                l=pt+1
            elif target<curr:
                r=pt-1
            else:
                return True
            pt=r-(r-l)//2
        return False


    # m is array of arrays
    # n is array
    # i is row
    # j is col
    def toSngl(self,n,i,j):
        return i*n+j
    def toMtrx(self,n,i):
        return [i//n,i%n]
    def getMtrx(self,pair,matrix):
        return matrix[pair[0]][pair[1]]
sol = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
for x in matrix:
    for i in x:
        print(sol.searchMatrix(matrix,i))    
print(sol.searchMatrix(matrix,0))     

