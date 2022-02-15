
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answerHead=None
        answerTail=None
        done=False
        carry=False
        l1v=0
        l2v=0
        while(not done):
            if(l1 is not None):
                l1v=l1.val
                l1=l1.next
            else:
                l1v=0

            if(l2 is not None):
                l2v=l2.val
                l2=l2.next
            else:
                l2v=0

            added=l1v+l2v
            if carry:
                added+=1
                carry=False
            if(added>9):
                added-=10
                carry=True

            if answerHead is None:
                answerHead=ListNode(added,None)
                answerTail=answerHead
            else:
                answerTail.next=ListNode(added,None)
                answerTail=answerTail.next
        
            if(l2==None and l1==None):
                done=True
        return answerHead
num1 = ListNode(7, ListNode(6, ListNode(5, ListNode(2, None))))
num2 = ListNode(8, ListNode(9, None))





sol = Solution()
answer=sol.addTwoNumbers(num1, num2)
print(answer.val)
print(answer.next.val)
print(answer.next.next.val)
print(answer.next.next.next.val)
# print(sol.addTwoNumbers(num1, num2).next.val)
# print(sol.addTwoNumbers(num1, num2).next.next.val)

