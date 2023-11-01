from typing import List,Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fakeNode=ListNode()
        p1=head

        while p1:
            if p1==fakeNode:
                return True
            temp=p1
            p1=p1.next
            temp.next=fakeNode
        return False
            



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



sol = Solution()
arr1=[1,2,3,4]
l1=sol.createLinkedList(arr1)
p1=l1
while p1.next:
    p1=p1.next
p1.next=l1
arr2=[1,2,3,4]
l2=sol.createLinkedList(arr2)
arr3=[1]
l3=sol.createLinkedList(arr3)
l3.next=l3

print(sol.hasCycle(l3))



