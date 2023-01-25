class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            nums1.clear()
            for i in nums2:
                nums1.append(i)
        elif n!=0:
            writer=n+m-1
            n1Read=m-1
            n2Read=n-1

            while writer!=-1:
                if (n1Read!= -1 and nums1[n1Read]>nums2[n2Read]) or n2Read==-1:
                    nums1[writer]=nums1[n1Read]
                    n1Read-=1
                else:
                    nums1[writer]=nums2[n2Read]
                    n2Read-=1
                writer-=1
            



        

sol = Solution()


arr1=[1,2,3,0,0,0]
arr2=[2,5,6]

# arr1=[0]
# arr2=[1]

arr1=[2,0]
arr2=[1]

# arr1=[-10,-10,-9,-9,-9,-8,-8,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-2,-2,-1,-1,0,1,1,1,2,2,2,3,3,3,4,5,5,6,6,6,6,7,7,7,7,8,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# arr2=[-10,-10,-9,-9,-9,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,9,9,9,9]

# arr1=[-10,-2,-1,0,0,0,0,0,0,0,0,0,0,0]
# arr2=[-1,-2,0,0,0,0,0,1,2,3]

# sol.merge(arr1, len(arr2), arr2, len(arr2))


# sol.merge(arr1, 0, arr2, 1)
# sol.merge(arr1, 4, arr2, 10)

# sol.merge(arr1, 3, arr2, 3)
sol.merge(arr1, 1, arr2, 1)



print(arr1)


# sol.sink(arr3,0)
# print(arr3)

# IF M IS 0?    
# if n is 0?

