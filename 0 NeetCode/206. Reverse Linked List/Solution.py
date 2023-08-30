from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return None
        if head.next==None:
            return head
        
        prev=head
        current=head.next
        head=current.next
        prev.next=None

        while head!=None:
            current.next=prev
            prev=current
            current=head
            head=head.next

        current.next=prev

        return current
    # 1 2 3 4 
    # *1(2) <- _(1,)
    # 1 *2(3) <- _

    #4 3 2 1

    def printLinkedList(self,l):
        print("=====")
        while l !=None:
            print(l.val)
            l=l.next
        print("=====")

    def createLinkedList(self,arr):
        if len(arr)==0:
            return None
        head=ListNode(arr[0],None)
        builder=head
        for i in range(1,len(arr)):
            temp=ListNode(arr[i],None)
            builder.next=temp
            builder=builder.next
        
        # print(head)
        return head
            
            


sol = Solution()

arr=[1,2,3,4]
l=sol.createLinkedList(arr)
sol.printLinkedList(l)

rev=sol.reverseList(l)
sol.printLinkedList(rev)



# 1 2 3 4 5 6


