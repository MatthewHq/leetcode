# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        length = self.countLength(head)
        half = int(length/2)
        isOdd = length % 2 == 1

        halfHead=self.getHalfHead(head,half,isOdd)
        print(halfHead.val, "HALF HEAD VAL")

    def countLength(self, head):
        count = 0
        current = head
        while current != None:
            count += 1
            current = current.next
        return count

    def getHalfHead(self, head, half, isOdd):
        current=head
        skipRange = half + 1 if isOdd else half
        for i in range(skipRange):
            current=current.next
        return current

    def reverse(self, halfHead):
        refererced=halfHead
        modified=halfHead.next
        holding=modified.next


    # has to be at least 3 long, so cover bases on length of 2 and 1 and maybe even 3 where the last step isn't overextending
    #once reversed just traverse both at same time and check :)



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

print(sol.isPalindrome(L8))
