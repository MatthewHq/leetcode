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
        # self.printList(head)
        pointer = head
        counter = 0
        while pointer != None:
            counter += 1
            pointer = pointer.next

        if counter == 1:
            return head
        if counter == 2:
            # newHead = head.next
            # newHead.next=head
            # head.next=None
            # return newHead
            return head
        if counter == 3:
            middle = head.next
            head.next = head.next.next
            head.next.next = middle
            middle.next = None
            return head

        even = counter % 2 == 0
        pointer = head
        stopAt = int(counter/2) - (1 if even else 0)
        for i in range(stopAt):
            pointer = pointer.next

        halfHead = pointer.next
        pointer.next = None

        halfHead = self.reverseList(halfHead)

        # self.printList(head)
        # self.printList(halfHead)
        firstHead = head
        for i in range(int(counter/2)):
            prevH = firstHead
            prevHH = halfHead

            firstHead = firstHead.next
            halfHead = halfHead.next

            prevH.next = prevHH
            prevHH.next = firstHead

        return head

    def reverseList(self, head):
        p1 = head.next
        p2 = p1.next
        p3 = None

        p1.next = head
        head.next = None
        while p2 != None:
            p3 = p2
            p2 = p2.next
            p3.next = p1
            p1 = p3
        return p1

    def printList(self, head):
        allVals = ""
        pointer = head
        while pointer != None:
            allVals += str(pointer.val)+", "
            pointer = pointer.next
            print(pointer)
        print(allVals[0:len(allVals)-2])


head = ListNode(1)

pointer = head
for i in range(2, 3):
    print("i", i)
    pointer.next = ListNode(i)
    pointer = pointer.next

Solution.printList(None, head)

# head = Solution.reverseList(None, head)
# Solution.printList(None, head)

sol = Solution()
sol.printList(sol.reorderList(head))
