from msilib.schema import Class


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = []
        self.hashMap = {}
        self.qIndexHashMap = {}

    def get(self, key: int) -> int:
        print("-----")
        print(self.queue)
        #print("get",key)
        index = self.qIndexHashMap.get(key)
        print(index,self.queue)
        if index != None:
            self.queue.pop(index)
            self.queue.append(key)
        print(self.queue)
        return self.hashMap.get(key) if self.hashMap.get(key)!=None else -1

    def put(self, key: int, value: int) -> None:
        print("-----")
        print(self.queue)
        #print("put",key,value)
        self.hashMap[key] = value
        self.queue.append(key)
        self.qIndexHashMap[key] = len(self.queue)-1
        
        if len(self.queue) > self.capacity:
            removeAll = self.queue.pop(0)
            self.hashMap.pop(removeAll)
            self.qIndexHashMap.pop(removeAll)
        print(self.queue)

class LinkedList:
    def __init__(self):
        self.size=0
        self.head=None
        self.tail=None

    def append(self,node):
        if self.size==0:
            self.head=node
            self.tail=self.head
        else:
            self.tail.right=node
            node.left=self.tail
            self.tail=node
        self.size+=1
    
    def pop(self):
        ret=self.head
        self.head=self.head.right
        self.head.left=None
        return ret.contents
        

    def refresh(self,node):
        left=node.left
        right=node.right
        left.right=right
        right.left=left
        self.append(node)

    def print(self):
        if self.size!=0:
            current=self.head
            while current!=None:
                print(current.contents)
                current=current.right

            


class Node:
    def __init__ (self,contents,left=None,right=None):
        self.contents=contents
        self.left=left
        self.right=right
    
    




    

# inputCmd = ["LRUCache", "put", "put", "get",
#          "put", "get", "put", "get", "get", "get"]
# inputVal=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]


# lru=LRUCache(inputVal[0][0])
# print("null")

# for i in range(len(inputVal)-1):
#     if inputCmd[i+1]=="get":
#         print(lru.get(inputVal[i+1][0]))
#     elif inputCmd[i+1]=="put":
#         lru.put(inputVal[i+1][0],inputVal[i+1][1])
#         print("null")


linked=LinkedList()
linked.print()
linked.append(Node("1"))
linked.append(Node("2"))
linked.append(Node("3"))
linked.print()
print("popping ",linked.pop())
linked.print()
linked.refresh(2)
linked.print()



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
