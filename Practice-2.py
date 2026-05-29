# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        result=dummy
        curr=head.next
        x=0
        while curr:
            if curr.val==0:
                result.next=ListNode(x)
                result=result.next
                x=0
            if curr.val!=0:
                x+=curr.val
            curr=curr.next
        return dummy.next