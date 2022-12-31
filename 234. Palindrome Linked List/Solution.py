# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        length = self.countLength(head)

        if length == 1:
            return True
        if length == 2:
            return head.val == head.next.val

        half = int(length/2)
        isOdd = length % 2 == 1

        self.skipRange = None
        halfHead = self.getHalfHead(head, half, isOdd)
        # print(halfHead.val, "HALF HEAD VAL")
        reversedHead = self.reverse(halfHead, half, length)
        # print("readingReversedHead")
        # self.readHead(reversedHead)

        return self.finalComparison(head,reversedHead)

    def countLength(self, head):
        count = 0
        current = head
        while current != None:
            count += 1
            current = current.next
        return count

    def getHalfHead(self, head, half, isOdd):
        current = head
        self.skipRange = half + 1 if isOdd else half
        # print("skiprange", self.skipRange)
        for i in range(self.skipRange):
            current = current.next
        return current

    def reverse(self, halfHead, half, length):
        halfLength = length-self.skipRange

        if halfLength == 1:
            return halfHead
        elif halfLength == 2:
            newHead = halfHead.next
            newHead.next = halfHead
            halfHead.next = None
            return newHead

        elif halfLength > 2:
            # if halflength is 3 or more:
            # reversing something of size 3 or higher
            currentSlot = halfHead
            holding = None
            print("halfLength-2", halfLength-2)
            referenced = currentSlot
            modified = currentSlot.next
            holding = currentSlot.next.next
            referenced.next = None

            modified.next = referenced
            currentSlot = modified

            for i in range(halfLength-3):
                print("iteration in reverse")
                referenced = modified
                modified = holding
                holding = holding.next
                modified.next = referenced
                currentSlot = modified
            holding.next = currentSlot
            return holding

    def finalComparison(self, head, halfHead):
        while halfHead != None:
            if head.val != halfHead.val:
                return False
            head=head.next
            halfHead=halfHead.next
        
        return True
                

    def readHead(self, head):
        current = head
        while current != None:
            print(current.val)
            current = current.next
        print("Done Reading")

    def createLL(self, arr):
        arr.reverse()
        end = ListNode(arr[0])
        current = end
        for i in range(1, len(arr)):
            newest = ListNode(arr[i], current)
            current = newest
        return current

    # has to be at least 3 long FOR ONE OF THE HALVES,
    # So what about length of 6 and below? What about 6
    # so cover bases on length of 2 and 1 and maybe even 3 where the last step isn't overextending
    # once reversed just traverse both at same time and check :)
sol = Solution()
L1 = ListNode(1, None)
L2 = ListNode(2, L1)
L3 = ListNode(3, L2)
L4 = ListNode(4, L3)
L5 = ListNode(4, L4)
L6 = ListNode(3, L5)
L7 = ListNode(2, L6)
L8 = ListNode(1, L7)


# L1 = ListNode(1, None)
L2 = ListNode(2, None)
L3 = ListNode(3, L2)
L5 = ListNode(4, L4)
L6 = ListNode(3, L5)
L7 = ListNode(2, L6)
L8 = ListNode(1, L7)

arr = [1, 2, 3]
arr = [1]
arr=[1,2,2,1]
arr=[1,1,2,3,1]
# arr=[1,2,3,4,5,6]
# arr=[1,2,3,4,5,6,7,8]
# arr=[1,2,3,4,5,6,7,8,9]
myLL = sol.createLL(arr)
sol.readHead(myLL)


print(sol.isPalindrome(myLL))
