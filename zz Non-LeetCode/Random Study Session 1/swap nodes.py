


class Node:
    indexes = None
    root = None

    def __init__(self, value, depth, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.depth = depth

    def __str__(self):
        return "[ vd[{}|{}] left[{}] right[{}] ]".format(self.value, self.depth, self.left, self.right)

    # def getLR(self):
    #     return [self.left, self.right]
    

    def traverse(self):
        output=[]
        self.recTrav(output)
        return output

    def recTrav(self,output):  
        
        if self.left!=-1:
            self.left.recTrav(output)
        output.append(self.value)
        if self.right!=-1:
            self.right.recTrav(output)
        

        

    def swap(self):
        holder = self.right
        self.right = self.left
        self.left = holder

    def recSwap(self,k):
        if self.depth % k == 0:
            self.swap()
        # print("HEY",k%self.depth)
        if self.left!=-1:
            self.left.recSwap(k)
        if self.right!=-1:
            self.right.recSwap(k)
        
        

        


def buildTree(val, lr, depth):  # fix
    if val == -1:
        return -1
    # if lr[0]==-1 and lr[1]==-1:
    #     return Node(val,depth+1,left=-1,right=-1)
    else:
        leftNode = buildTree(lr[0], None if lr[0] == -1 else Node.indexes[lr[0]-1], depth+1)
        rightNode = buildTree(lr[1], None if lr[1]== -1 else Node.indexes[lr[1]-1], depth+1)
        return Node(val, depth+1, left=leftNode, right=rightNode)


def swapNodes(indexes, queries):
    # Write your code here
    Node.indexes = indexes
    root = buildTree(1, indexes[0], 0)
    print(root)
    print("======")
    # root.swap()
    # print(root)

    out=[]
    for i in queries:
        root.recSwap(i)
        arr=root.traverse()
        print(arr)
        out.append(arr)
    print(root)
    # print(root)
    print("======")
    print(out)
    return out
    
    
    # root=Node(1,1)
    # depth=2
    # for i in range(1,len(indexes)):
    #     node = Node()

    #     rootCount+=1


indexes=[[2, 3], [-1, -1], [-1, -1]]
queries=[1, 1]
swapNodes(indexes, queries)

print("=====================================")
indexes=[[2, 3], [-1, 4], [-1, 5], [-1, -1], [-1, -1]]
queries=[2]
swapNodes(indexes, queries)

print("=====================================")
indexes = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
queries = [2, 3]
swapNodes(indexes, queries)
print("=====================================")
