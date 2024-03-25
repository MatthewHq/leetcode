from typing import List,Optional
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1Len=len(nums1)
        n2Len=len(nums2)
        
        totalLen=n1Len+n2Len
        
        if totalLen%2==0:
            #if even
            self.targetOffset=totalLen/2-1
            pass
        else:
            #if odd
            self.targetOffset=(totalLen-1)/2
            
        print(self.targetOffset,"target offset")
            
        
        self.l1,self.l2=0,0
        self.r1=len(nums1)-1
        self.r2=len(nums2)-1
        
        self.leftOffset=0
        self.rightOffset=0

        while self.leftOffset<self.targetOffset and self.rightOffset<self.targetOffset and self.l1<=self.r1 and self.l2<=self.r2:
            self.checkPrep(nums1,nums2)
        
        self.DEBUGprintRange(nums1,self.l1,self.r1)
        self.DEBUGprintRange(nums2,self.l2,self.r2)
        print("offsets",self.leftOffset,self.rightOffset)
        
    
    def checkPrep(self,nums1,nums2):
        #check num1
        
        n1cl=self.binarySearch(self.l1,self.r1,nums2[self.l2],nums1)
        n1cr=self.binarySearch(self.l1,self.r1,nums2[self.r2],nums1)
        
        crossResultsNums1=self.crossCheck(nums1,nums2,self.l1,self.r1,n1cl,n1cr,self.l2,self.r2)
        self.l1,self.r1=crossResultsNums1
        
        #check num2]
        n2cl=self.binarySearch(self.l2,self.l2,nums1[self.l1],nums2)
        n2cr=self.binarySearch(self.l2,self.r2,nums1[self.r1],nums2)
        crossResultsNums2=self.crossCheck(nums2,nums1,self.l2,self.r2,n2cl,n2cr,self.l1,self.r1)
        self.l2,self.r2=crossResultsNums2
        
       
        
        # print("Checking num1 with num2: range: {} l2={}|({}) cl={}|({}) -- nums1@ {}|({}) | r2={}({}) cr={}|({}) -- nums1@ {}({}) results={}".format(
        #                                                                                                                                   nums1,
        #                                                                                                                                   self.l2,
        #                                                                                                                                   nums2[self.l2],
        #                                                                                                                                   n1cl,
        #                                                                                                                                   nums1[n1cl],
        #                                                                                                                                   n1cl,
        #                                                                                                                                   nums1[n1cl],
        #                                                                                                                                   self.r2,
        #                                                                                                                                   nums2[self.r2],
        #                                                                                                                                   n1cr,
        #                                                                                                                                   nums1[n1cr],
        #                                                                                                                                   n1cr,
        #                                                                                                                                   nums1[n1cr],
        #                                                                                                                                   crossResultsNums1))
        # print("Checking num2 with num1: range: {} l1={}|({}) cl={}|({}) -- nums2@ {}|({}) | r1={}({}) cr={}|({}) -- nums2@ {}({}) results={}".format(
        #                                                                                                                                   nums2,
        #                                                                                                                                   self.l1,
        #                                                                                                                                   nums1[self.l1],
        #                                                                                                                                   n2cl,
        #                                                                                                                                   nums2[n2cl],
        #                                                                                                                                   n2cl,
        #                                                                                                                                   nums2[n2cl],
        #                                                                                                                                   self.r1,
        #                                                                                                                                   nums1[self.r1],
        #                                                                                                                                   n2cr,
        #                                                                                                                                   nums2[n2cr],
        #                                                                                                                                   n2cr,
        #                                                                                                                                   nums2[n2cr],
        #                                                                                                                                   crossResultsNums2))
        
        print("offsets",self.leftOffset,self.rightOffset)
        print("num1 boundaries",self.l1,self.r1)
        print("num2 boundaries",self.l2,self.r2)
        
    
    def binarySearch(self,l,r,t,arr):
        while l<=r:
            m=r-(r-l)//2
            
            if arr[m]<t:
                l=m+1
            elif arr[m]>t:
                r=m-1
            else:
                return m
        return m
    
    def crossCheck(self,t,c,tl,tr,cl,cr,ocl,ocr):
        #might have to doa  stopper where if it passses the dif limit it undos
        leftDif=0
        rightDif=0
        
        if c[ocl]>=t[tl]:
            if tl==cl:
                ntl=cl+1
            else:
                ntl=cl
            leftDif=ntl-tl
            if leftDif+self.leftOffset>self.targetOffset:
                leftDif=self.targetOffset-self.leftOffset
                ntl-=tl+leftDif
            
            self.leftOffset+=int(leftDif)
        else:
            ntl=tl
    
        if t[tr]>=c[ocr]:
            if tr==cr:
                ntr=tr-1
            else:
                ntr=cr
            rightDif=tr-ntr
            if rightDif+self.rightOffset>self.targetOffset:
                    rightDif=self.targetOffset-self.rightOffset
                    ntr-=tr+rightDif
            self.rightOffset+=int(rightDif)
        else:
            ntr=tr
        
        return int(ntl),int(ntr)
    
    def DEBUGprintRange(self,arr,l,r):
        x=[]
        for i in range(l,r+1):
            x.append(arr[i])
        print(x)
        
        
        
sol = Solution()



# test=[1,3,5,7,9,11]
# l,r=2,3
# tar=[6,6]

# test=[2,4,6,8,10]
# l,r=1,3
# tar=[5,7]


# test=[1,1,1,1,3,4]
# tar=[1]
# for t in tar:
#     print(t,sol.binarySearch(l,r,t,test))

nums1=[1,3,5,7,9,11]
nums2=[2,4,6,8,10]

nums1=[]
nums2=[2,2,2,2,2,2,2,2,2]
    
sol.findMedianSortedArrays(nums1,nums2)
    
