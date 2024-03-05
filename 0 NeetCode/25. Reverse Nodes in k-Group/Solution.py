from typing import List,Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pivot=head
        tracer=head
        if k==1:
            self.totalReverse(head)
        else:
            results=[pivot,None,None,None]
            while tracer!=None:
                results=self.reverseK(k,results[0],results[1],results[2],results[3])
                tracer=results[3]
            return results[0]
    
    def reverseK(self,k,piv,prev,curr,tracer):
        #initialize variables for first swap
        pivot=piv
        if prev==None:
            prev=pivot
        else:
            k+=1
        if tracer==None:
            tracer=pivot
        if curr==None:
            curr=pivot.next
        if curr!=None:
                nxt=curr.next
        else:
            return
        lagger=curr
            
        for i in range(k-1):
            if tracer!=None:
                if nxt==None and i!=k-2:
                    if i>0:
                        rev=self.regReverse(i,pivot)
                        pivot.next=curr
                        pivot=rev
                        # for j in range(i+2):
                        #     startHolder=pivot.next
                        #     endHolder=prev
                        #     pivot.next=curr
                        #     pivot=startHolder ##has to be the one before pivot
                        #     prev.next=endHolder.next
                    break
                ### perform one "swap"
                curr.next=pivot
                prev.next=nxt
                
                ### adjust variables for next "swap"
                tracer=nxt
                pivot=curr
                #prev=prev.next
                curr=nxt
                if curr!=None:
                    nxt=curr.next #else return
                
                
            
        tracer=nxt
        return [pivot,prev,curr,tracer]
            
    def regReverse(self,x,head):
        newHead=head
        holdHead=head
        tracer=head.next
        if x>0:
            newHead.next=None
        for i in range(x):
            prevT=tracer
            tracer=tracer.next
            newHead=prevT
            newHead.next=holdHead
            holdHead=newHead
        # self.printLinkedList(newHead)
        return newHead
    
    def totalReverse(self,head):
        newHead=head
        holdHead=head
        tracer=head.next
        newHead.next=None
        while tracer!=None:
            prevT=tracer
            tracer=tracer.next
            newHead=prevT
            newHead.next=holdHead
            holdHead=newHead
        return newHead
            
            
            

    def printLinkedList(self,l):
        listed=[]
        while l !=None:
            listed.append(l.val)
            l=l.next
        print(listed)

    def createLinkedList(self,arr):
        if len(arr)==0:
            return None
        head=ListNode(arr[0],None)
        builder=head
        for i in range(1,len(arr)):
            temp=ListNode(arr[i],None)
            builder.next=temp
            builder=builder.next
        return head

sol = Solution()
list=sol.createLinkedList([1,2,3,4,5,6,7])
# 
# results=sol.reverseK(5,list,None,None,None)
result=sol.reverseKGroup(list,3)
sol.printLinkedList(result)

# list=sol.createLinkedList([1,2,3,4,5,6,7,8,9,10])
# results=sol.reverseK(11,list,list)
# sol.printLinkedList(results[1])

# list=sol.createLinkedList([1,2,3,4,5,6,7,8,9,10])
# results=sol.reverseK(2,list,list)
# sol.printLinkedList(results[1])


# list=sol.createLinkedList([1,2])
# results=sol.reverseK(3,list,list)
# sol.printLinkedList(results[1])

# list=sol.createLinkedList([1,2,3,4,5])
# results=sol.reverseK(2,list,None,None,None)
# sol.printLinkedList(results[0])
# results=sol.reverseK(2,results[0],results[1],results[2],results[3])
# sol.printLinkedList(results[0])
# results=sol.reverseK(2,results[0],results[1],results[2],results[3])
# sol.printLinkedList(results[0])
# results=sol.reverseK(2,results[0],results[1],results[2],results[3])
# sol.printLinkedList(results[0])

# list=sol.createLinkedList([1,2,3,4,5])

# result=sol.totalReverse(list)
# sol.printLinkedList(result)



 