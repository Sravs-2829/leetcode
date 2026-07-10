# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        d=ListNode(0)
        curr=d
        c=0
        while c or l1 or l2:
            if l1:
                c=c+l1.val
                l1=l1.next
            if l2:
                c=c+l2.val
                l2=l2.next
            curr.next=ListNode(c%10)
            c=c//10
            curr=curr.next
        return d.next