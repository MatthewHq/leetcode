# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    list1 = None
    list2 = None

    def mergeTwoLists(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

        if list1==None and list2==None:
            return None
        newHead = self.minNode()
        currentHead = newHead

        # n = self.minNode()
        # print(n.val)
        # print(self.list1.val)
        # print(self.list2.val)

        while self.list1!=None or self.list2!=None:
            # print(ListNode.printList(None,self.list1))
            # print(ListNode.printList(None,self.list2))

            smallest=self.minNode()
            # print(smallest.val)
            currentHead.next=smallest
            currentHead=currentHead.next

            # print("=-===")

        # print(ListNode.printList(None,newHead))
        return newHead

    def minNode(self):
        # print(self.list1,"l1")
        # print(self.list2,"l2")
        if (self.list2==None) or (self.list1!=None and self.list1.val < self.list2.val):
            minNode = self.list1
            self.list1 = self.list1.next
        else:
            minNode = self.list2
            self.list2 = self.list2.next
        return minNode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def createList(this, arr):
        if len(arr)==0:
            return None
        prev = None
        for i in reversed(range(len(arr))):
            now = ListNode(arr[i], prev)
            prev = now
        return now

    def printList(this, head):
        ret = []
        current = head
        while(current != None):
            ret.append(current.val)
            current = current.next
        return ret


sol = Solution()


list1 = ListNode.createList(None, [])
list2 = ListNode.createList(None, [])

# print(ListNode.printList(None, list1))
# print(ListNode.printList(None, list2))

sol.mergeTwoLists(list1, list2)
