# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            # Store the next node
            next_node = curr.next
            # Reverse the link
            curr.next = prev
            # Move to the next nodes
            prev = curr
            curr = next_node
        
        return prev