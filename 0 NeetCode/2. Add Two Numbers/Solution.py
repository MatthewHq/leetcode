from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        p1 = l1
        p2 = l2

        result = None
        val=0
        if p1:
            val += p1.val
        if p2:
            val += p2.val


        carry = 0
        if val > 9:
            carry = 1
            val -= 10
        result = ListNode(val, None)

        p1 = p1.next
        p2 = p2.next
        p3 = result

        while p1 != None or p2 != None:
            val = 0
            if p1:
                val += p1.val
            if p2:
                val += p2.val
            val += carry
            if val > 9:
                carry = 1
                val -= 10
            else:
                carry=0
            p3.next = ListNode(val,None)
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            p3 = p3.next
        if carry==1:
            p3.next = ListNode(1,None)
        return result

    def printLinkedList(self, l):
        listed = []
        while l != None:
            listed.append(l.val)
            l = l.next
        print(listed)

    def createLinkedList(self, arr):
        if len(arr) == 0:
            return None
        head = ListNode(arr[0], None)
        builder = head
        for i in range(1, len(arr)):
            temp = ListNode(arr[i], None)
            builder.next = temp
            builder = builder.next
        return head


sol = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1 = [9]
l2 = [1]
linked1=sol.createLinkedList(l1)
linked2=sol.createLinkedList(l2)
sol.printLinkedList(sol.addTwoNumbers(linked1,linked2))