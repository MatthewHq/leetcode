from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        ongoing = []
        biggest = heights[0]
        current = []
        

#the if statements can be rearranged
        for i in range(len(heights)):
            if len(current)!=0 or heights[i]!=0:
                print(i,heights[i],"=====")
            
                if len(current)==0 and heights[i]!=0:
                    current.append([heights[i],1])
                elif heights[i] > current[-1][0]:  # the new one is bigger
                    print("A")
                    current.append([heights[i],1])
                
                elif heights[i]==current[-1][0]:
                    print("B")
                    current[-1][1]=current[-1][1]+1

                elif heights[i]<current[-1][0]: #new one is smaller
                    print("C")
                    stackLen=0
                    while len(current) > 0 and heights[i] < current[-1][0]:
                        top=current.pop()
                        print("OLD TOP",top,stackLen)
                        oldStack=top[1]
                        top[1]=top[1]+stackLen 
                        print("NEW TOP",top)
                        stackLen+=oldStack
                        
                        if top[0]*top[1]>biggest:
                            biggest=top[0]*top[1]
                    if heights[i]!=0:
                        if len(current)!=0 and current[-1][0]==heights[i]:
                            current[-1][1]+=stackLen+1
                        else:
                            current.append([heights[i],stackLen+1])
                
            print(current)

        for j in reversed(range(len(current))):
            leftOver=current[j]
            print(leftOver,"left")
            if leftOver[0]*leftOver[1]>biggest:
                biggest=leftOver[0]*leftOver[1]
            if j>0:
                current[j-1][1]=current[j-1][1]+current[j][1]
        return biggest


sol = Solution()

a = [2, 3, 3, 6, 5, 1, 5, 5, 6]
# a=[1,2,1,1,2]
# a=[4,2,0,3,2,4,3,4]
# a=[2,1,5,6,2,3]
# a=[0]
print(sol.largestRectangleArea(a))
