
class Node:

    gt = '>'
    lt = '<'
    eq = "="

    def __init__(self,left=None,right=None):
        self.left = left
        self.right = right

    # generate relation
    def genRel(self, arr, endpoint=None):  # passed in segment of size 3
        if endpoint==None:
            if arr[1] > arr[0]:  # mid > left
                self.left = Node.gt
            elif arr[1] < arr[0]:  # mid < left
                self.left = Node.lt
            else:
                self.left = Node.eq

            if arr[1] > arr[2]:  # mid > right
                self.right = Node.gt
            elif arr[1] < arr[2]:  # mid < right
                self.right = Node.lt
            else:
                self.right = Node.eq
        elif endpoint=='left': #left endpoint case TAKES ARR OF SIZE 2
            self.left=Node.eq
            if arr[0] > arr[1]: 
                self.right = Node.gt
            elif arr[0] < arr[1]:  
                self.right = Node.lt
            else:
                self.right = Node.eq
        elif endpoint=='right':#right endpoint case TAKES ARR OF SIZE 2
            self.right=Node.eq
            if arr[1] > arr[0]: 
                self.left = Node.gt
            elif arr[1] < arr[0]:  
                self.left = Node.lt
            else:
                self.left = Node.eq
    
    def printNode(self):
        return ("// {}|{} //".format(self.left,self.right))


def equalize(arr):
    if len(arr)==2:
        return 3
    smallest=min(arr)
    dif=1-smallest
    print(arr)
    for i in range(len(arr)):
        arr[i]+=dif
    print(arr)
    return sum(arr)

def candies(n,arr):
    # Write your code here
    candies=0
    currentStreak=[]
    relations = []
    inStreak=False
    for i in range(len(arr)):
        node=Node()
        if i==0:
            node.genRel(arr[0:2],'left')
        elif i==len(arr)-1:
            node.genRel(arr[len(arr)-2:len(arr)],'right')
        else:
            node.genRel(arr[i-1:i+2])
        relations.append(node)

        print(i,node.printNode())
        
        if node.left==Node.eq:
            if node.right==Node.eq:
                candies+=1
            else:
                inStreak=True
                currentStreak.append(0)
        elif node.left==Node.gt:
            currentStreak.append(currentStreak[len(currentStreak)-1]+1)
        elif node.left==Node.lt:
            # print(currentStreak)
            # print("LESS THAN")
            if node.right==Node.eq:
                modifier=min(currentStreak)
            else:
                if node.right==Node.gt and len(currentStreak)>1: #maybe more than 2 instead of 1
                    qq=equalize(currentStreak)
                    # print("EQQQQ",qq)
                    candies+=qq
                    currentStreak.clear()
                    modifier=1
                else:modifier=currentStreak[len(currentStreak)-1]-1
            currentStreak.append(modifier)



        if node.right==Node.eq and node.left!=Node.eq:
            qq=equalize(currentStreak)
            # print("EQQQQ",qq)
            candies+=qq
            currentStreak.clear()

        
    print("candies",candies)
    return candies

        
        # print("test")    
    
    # if i == 0:
    #     pass  # GENERATE LEFT, CALCULATE RIGHT
    # elif i == len(arr)-1:
    #     pass  # GENERATE RIGHT, CALCULATE LEFT

arr = [1, 2, 3, 4, 4, 4, 4, 3, 2, 3, 3, 5, 5, 5, 1, 2, 3, 4, 1] #37
arr = [4,6,4,5,6,2] #10
arr=[1,2,2] #4
arr=[2,4,2,6,1,7,8,9,2,1] #19
candies(0,arr)



