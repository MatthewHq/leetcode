"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        randoms = {}
        current = head
        previous = None
        i = 0
        while current.next != None:
            randoms[current] = i

            # newNode=Node(current.val,None,None)
            current = current.next
            i += 1

    def printList(self, head):
        current = head
        vals = ""
        while current != None:
            # print("[Val: {}, Nxt: {}, Rnd:{}".format(
            # current.val, current.next.val, current.random))
            vals += " [{} . {}] ->".format(current.val,
                                           "N" if not current.random else current.random.val)
            current = current.next
        vals += " N"
        print(vals)


tail = Node(1, None, None)
vals = [7, 13, 11, 10, 1]
rands = [None, 0, 4, 2, 0]
holder = tail
head = None
pointers={}
pointers[None]=None
pointers[4]=tail
for i in range(4):
    head = Node(vals[3-i], holder, None)
    pointers[3-i]=head
    holder = head

current=head
for i in range(5):
    current.random=pointers[rands[i]]
    current=current.next

Solution.printList(None,head)
    


sol = Solution()
sol.printList(head)
sol.copyRandomList(head)
