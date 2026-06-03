# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr=head
        value=[]
        while curr:
            value.append(curr.val)
            curr=curr.next
        temp=value[k-1]
        value[k-1]=value[-k]
        value[-k]=temp
        head2=ListNode(value[0])
        curr2=head2
        for i in value[1:]:
            curr2.next=ListNode(i)
            curr2=curr2.next
        return head2