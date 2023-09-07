from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head=None
        current=None
        while list1!=None or list2!=None:
            if list1==None:
                minNode=list2
                list2=list2.next
            elif list2==None:
                minNode=list1
                list1=list1.next
            elif list1.val<list2.val:
                minNode=list1
                list1=list1.next
            else:
                minNode=list2
                list2=list2.next
            if head==None:
                head=minNode
                current=head
            else:
                current.next=minNode
                current=current.next
        return head
            
            
    

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
    
sol=Solution()

list1Arr=[1,1,1,1]
list2Arr=[2]

l1=sol.createLinkedList(list1Arr)
l2=sol.createLinkedList(list2Arr)

sol.printLinkedList(l1)
sol.printLinkedList(l2)

merged=sol.mergeTwoLists(l1,l2)
sol.printLinkedList(merged)

    