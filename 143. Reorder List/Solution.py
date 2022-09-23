# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pass

    def printList(self, head):
        allVals = ""
        pointer = head
        while pointer != None:
            allVals += str(pointer.val)+", "
            pointer = pointer.next
        print(allVals[0:len(allVals)-2])


head = ListNode(0)

pointer = head
for i in range(1, 10):
    pointer.next = ListNode(i)
    pointer = pointer.next

Solution.printList(None, head)
