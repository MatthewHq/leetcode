from typing import List,Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #count nodes
        count=1
        countHead=head
        while countHead.next:
            # print(":a")
            count+=1
            countHead=countHead.next

        #split into two
        half=count//2+1
        head2=head
          #cutting 2nd half off
        for i in range(half):
            if i==half-1:
                tempHead=head2
                head2=head2.next
                tempHead.next=None
            else:
                head2=head2.next
        head1=head.next

        head2=self.reverse(head2)

        # self.printLinkedList(head1)
        # self.printLinkedList(head2)

        





        #combine into 1
        zipper=head
        turn =True
        while head1 or head2:
            if turn and head2:
                nextZip=head2
                head2=head2.next
                zipper.next=nextZip
                zipper=zipper.next
                turn = not turn
            else:
                if head1:
                    nextZip=head1
                    head1=head1.next
                    zipper.next=nextZip
                    zipper=zipper.next
                turn = not turn
        return head

    def reverse(self,head):
        previous=None
        current=head
        if current!=None:
            nextNode=current.next
        while current!=None:
            current.next=previous
            previous=current
            current=nextNode
            if nextNode!=None:
                nextNode=current.next
            else:
                current=nextNode
        return previous


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
arrList=[1,2,3,5]
# arrList=[1,2]
l1=sol.createLinkedList(arrList)
# sol.printLinkedList(l1)
# reved=sol.reverse(l1)
sol.printLinkedList(sol.reorderList(l1))



# print(sol.reorderList(l1))
