# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        kep=l1
        a=[]
        b=[]
        a.append(l1.val)
        b.append(l2.val)
        while(1):
            try:
                l1=l1.next
                l2=l2.next
                a.append(l1.val)
                b.append(l2.val)
            except:
                break
        a.reverse()
        b.reverse()
        c=int(''.join([str(i) for i in a]))
        d=int(''.join([str(i) for i in b]))
        tar=c+d
        tarLIST=list(str(tar))
        tarLIST.reverse()
        tarrLIST=[int(i) for i in tarLIST]
        kep2=kep

        for i in tarrLIST:
            kep.val=i
            kep=kep.next

        return kep2
        
2. Add Two Numbers
