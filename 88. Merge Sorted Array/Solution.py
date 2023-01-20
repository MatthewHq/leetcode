class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m==0:
            nums1.clear()
            for i in nums2:
                nums1.append(i)
        else:
            originalM=m
            i=0
            j=0
            m=m+n
            while(i!=m and j!=n):
                if nums2[j]>=nums1[i] or i>=originalM:
                    if nums1[i]==0 and i>=originalM:
                        self.swap(nums1,i,nums2,j)
                        j+=1
                        i+=1
                    else:
                        i+=1
                else: #j<i
                    self.swap(nums1,i,nums2,j)
                    self.sink(nums2,j)


    def sink(self, arr1, current):
        if current != len(arr1)-1:
            if arr1[current] > arr1[current+1]:
                self.swap(arr1,current,arr1,current+1)
                self.sink(arr1,current+1)

    def swap(self,arr1,i,arr2,j):
        holder=arr1[i]
        arr1[i]=arr2[j]
        arr2[j]=holder


sol = Solution()


arr1=[1,2,3,0,0,0]
arr2=[2,5,6]

arr1=[0]
arr2=[1]

# arr1=[-10,-10,-9,-9,-9,-8,-8,-7,-7,-7,-6,-6,-6,-6,-6,-6,-6,-5,-5,-5,-4,-4,-4,-3,-3,-2,-2,-1,-1,0,1,1,1,2,2,2,3,3,3,4,5,5,6,6,6,6,7,7,7,7,8,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# arr2=[-10,-10,-9,-9,-9,-9,-8,-8,-8,-8,-8,-7,-7,-7,-7,-7,-7,-7,-7,-6,-6,-6,-6,-5,-5,-5,-5,-5,-4,-4,-4,-4,-4,-3,-3,-3,-2,-2,-2,-2,-2,-2,-2,-1,-1,-1,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7,8,8,8,8,9,9,9,9]

arr1=[-10,-2,-1,0,0,0,0,0,0,0,0,0,0,0]
arr2=[-1,-2,0,0,0,0,0,1,2,3]

# sol.merge(arr1, len(arr2), arr2, len(arr2))
sol.merge(arr1, 4, arr2, 10)
print(arr1)


# sol.sink(arr3,0)
# print(arr3)

# IF M IS 0?    
# if n is 0?

