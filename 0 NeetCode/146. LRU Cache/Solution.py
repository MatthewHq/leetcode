from typing import List,Optional


class LRUCache:

    def __init__(self, capacity: int):
        self.hashRefs={}
        self.capacity=capacity
        self.head=None 
        self.tail=None
        self.size=0
        self.index={}

    def get(self, key: int) -> int:
        target=self.index.get(key)
        if target!=None:
            if self.head!=target:
                self.size-=1
                self.index[key]=None
                if target==self.tail:
                    newTail=self.tail.prev
                    newTail.next=None
                    self.tail=newTail
                else:
                    target.prev.next=target.next
                    target.next.prev=target.prev
                    
                    
                self.put(key,target.val)
        else:
            print(-1)
            return -1
            
        print(target.val)
        return target.val
        
        

    def put(self, key: int, value: int) -> None:
        
        
        
        if self.index.get(key)!=None and self.head!=None and self.head.key!=key:
            self.get(key)
            self.put(key,value)
        elif self.index.get(key)!=None and self.head!=None and self.head.key==key:
            self.head.val=value
        else:
            newNode=ListNode(value,key)
            self.size+=1
            self.index[key]=newNode
        
        
        
        
            if self.head!=None:
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode
            else:
                self.head=newNode
                self.tail=newNode

            if self.size>self.capacity:
                self.index[self.tail.key]=None
                self.size-=1
                self.tail=self.tail.prev 
                self.tail.next=None
                self.head=newNode
        


        

class ListNode:
    def __init__(self, val=0, key=None,prev=None,next=None):
        self.val = val
        self.next = next
        self.prev=prev
        self.key=key
        
    def __str__(self):
        return self.key+self.val

    def printLinkedList(self,r):
        if not hasattr(r,"head"):
            print("[]")
            return
        l=r.head
        listed=[]
        while l !=None:
            listed.append("["+str(l.key)+","+str(l.val)+"]")
            l=l.next
        print(listed)

    def createLinkedList(self,arr):
        if len(arr)==0:
            return None
        head=ListNode(arr[0],None)
        builder=head
        for i in range(1,len(arr)):
            temp=ListNode(arr[i],None)
            builder.next=temp
            builder=builder.next
        return head


instruction=["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
value=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

# instruction=["LRUCache","put","put","put","put","get","get"]
# value=[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
instruction=["LRUCache","get","put","get","put","put","get","get"]
value=[[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]


instruction=["LRUCache","put","put","put","put","get","get"]
value=[[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]

instruction=["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
value=[[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]




cache=None
for i in range(len(instruction)):
    ListNode.printLinkedList(None,cache)
    if instruction[i]=="LRUCache":
        cache=LRUCache(value[i][0])
    elif instruction[i]=="put":
        cache.put(value[i][0],value[i][1])
        print("put",value[i][0],value[i][1])
    elif instruction[i]=="get":
        cache.get(value[i][0])
        print("get",value[i][0])
        
        
    