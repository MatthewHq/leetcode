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
        randoms = []
        nodeKeys = {}
        nodeKeys[None] = None
        # originals
        current = head

        # news
        newKeys = {}
        newKeys[None] = None
        newPrevious = None
        newHead = None

        x = 0
        while current != None:
            newNode = Node(current.val, None, None)
            if newPrevious != None:
                newPrevious.next = newNode
            else:
                newHead = newNode
            newPrevious = newNode
            newKeys[x] = newNode
            randoms.append(current.random)
            nodeKeys[current] = x
            x += 1
            current = current.next

        combo = []
        for i in range(len(randoms)):
            combo.append(nodeKeys[randoms[i]])
        print(combo)
        
        x = 0
        current=newHead
        while current != None:
            current.random=newKeys[combo[x]]
            x += 1
            current = current.next

        self.printList(newHead)
        self.printList(head)
        return newHead

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
pointers = {}
pointers[None] = None
pointers[4] = tail
for i in range(4):
    head = Node(vals[3-i], holder, None)
    pointers[3-i] = head
    holder = head

current = head
for i in range(5):
    current.random = pointers[rands[i]]
    current = current.next

Solution.printList(None, head)


sol = Solution()
sol.printList(head)
sol.copyRandomList(head)
