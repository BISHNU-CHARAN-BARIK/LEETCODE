# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None:
            return head
        if head.next is None:
            return head
        curr=head
        length=0
        while curr is not None:
            curr=curr.next
            length+=1
        rk=k%length
        for i in range(rk):
            prev=None
            curr=head
            while curr.next is not None:
                prev=curr
                curr=curr.next        
            prev.next=None
            curr.next=head
            head=curr
        return head