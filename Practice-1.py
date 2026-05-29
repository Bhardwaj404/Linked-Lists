# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        from math import gcd
        curr = head
        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)
            node = ListNode(g)
            node.next = curr.next
            curr.next = node
            curr = node.next   # skip the inserted node
        return head