from typing import List,Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        db=self.createHashDB(lists)
        # print(db)
        sortedKeys=sorted(db)
        # print(sortedKeys)
        newHead=None
        tracer=None
        for i in range(len(sortedKeys)):
            for listIndex in db[sortedKeys[i]]:
                
                head=lists[listIndex]
                while head!=None and head.val==sortedKeys[i]:
                    # print(head.val,sortedKeys[i])
                    head=lists[listIndex]
                    if tracer!=None:
                        holder=head.next
                        tracer.next=head
                        tracer=tracer.next
                        head=holder
                        
                        
                        # print(head.val)
                        
                        # print(lists[listIndex].val)
                    else:
                        newHead=head
                        tracer=newHead
                        head=head.next
                    lists[listIndex]=head
                        
        # self.printLinkedList(newHead)
        return newHead
    def createHashDB(self,lists):
        db={}
        for i in range(len(lists)):
            
            head=lists[i]
            while head!=None:
                # self.printLinkedList(head)
                if db.get(head.val)==None:
                    db[head.val]=[i]
                else:
                    db[head.val].append(i)
                head=head.next
        return db
        

    def printLinkedList(self,l):
        listed=[]
        while l !=None:
            listed.append(l.val)
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
    
    def listArr(self,lists):
        created=[]
        print(lists)
        for list in lists:
            head=self.createLinkedList(list)
            created.append(head)
        return created

sol = Solution()
lists = [[1,4,5],[1,3,4],[2,6]]

realInput=sol.listArr(lists)  

for list in realInput:
    sol.printLinkedList(list)

sol.mergeKLists(realInput)


#make hashmap {value:[listsIndexContainedIn]}
#{1:[1,4,9], 2:[2,3,11]}
#sort all the hashmap keys
