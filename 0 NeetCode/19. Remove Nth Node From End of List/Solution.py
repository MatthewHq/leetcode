from typing import List,Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # keep=head
        prev=None
        forward=head
        for i in range(n-1):
            forward=forward.next

        while forward.next:
            forward=forward.next
            if not prev:
                prev=head
            # keep=keep.next
            
        

        
        # self.printLinkedList(prev)
        # self.printLinkedList(keep)
        # self.printLinkedList(forward)
        
        if prev==None:
            return head.next
        else:    
            prev.next=prev.next.next

        # print("---")
        return head

    ##########################
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
    #############################

sol = Solution()
arr=[1,2]
n=1

# arr=[1,2]
# n=1

l1=sol.createLinkedList(arr)
# sol.printLinkedList(l1)
removed=sol.removeNthFromEnd(l1,n)
sol.printLinkedList(removed)
