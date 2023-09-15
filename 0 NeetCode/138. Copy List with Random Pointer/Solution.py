from typing import List,Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        pt1=head
        cHead=pt2=Node(head.val)
        # counter=0
        bank={pt1:pt2}
        # print(f"Bank {counter} : {pt2.val}")

        while pt1.next!=None:
            pt1=pt1.next
            temp=Node(pt1.val)
            pt2.next=temp
            pt2=pt2.next
            # counter+=1
            bank[pt1]=pt2
            # print(f"Bank {counter} : {pt2.val}")
        
        pt1=head
        pt2=cHead
        
        # self.printLinkedListInput(pt2)
        # self.printLinkedList(pt2)
        # self.printLinkedListInput(pt1)

        while pt1!=None:
            if pt1.random==None:
                pt2.random=None
            else:
                # print(pt1.random)
                pt2.random=bank[pt1.random]
                # print(pt2.val,pt1.random,bank[pt1.random].val)
            pt1=pt1.next
            pt2=pt2.next
        return cHead


    def printLinkedList(self,l):
        listed=[]
        while l !=None:
            listed.append([l.val,None if l.random == None else l.random.val])
            l=l.next
        print(listed)

    def printLinkedListInput(self,l):
        listed=[]
        while l !=None:
            listed.append([l.val,l.random])
            l=l.next
        print(listed)

    def createLinkedList(self,arr):
        bank={}
        if len(arr)==0:
            return None
        head=Node(arr[0][0],None,None)
        bank[0]=head
        builder=head
        for i in range(1,len(arr)):
            temp=Node(arr[i][0],None,None)
            print(i)
            bank[i]=temp
            builder.next=temp
            builder=builder.next
        pt=head
        for i in range(0,len(arr)):
            print(i)
            pt.random=None if arr[i][1] is None else bank[arr[i][1]]
            pt=pt.next    
        return head
    
    def createLinkedListInput(self,arr):

        if len(arr)==0:
            return None
        head=Node(arr[0][0],None,arr[0][1])

        builder=head
        for i in range(1,len(arr)):
            temp=Node(arr[i][0],None,arr[i][1])
            builder.next=temp
            builder=builder.next
        return head

sol = Solution()

ll=[[7,None],[13,0],[11,4],[10,2],[1,0]]
listF=sol.createLinkedListInput(ll)
sol.printLinkedListInput(listF)
copied=sol.copyRandomList(listF)
sol.printLinkedList(copied)

