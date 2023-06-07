# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Calculate the length of the linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # Step 2: Handle the case where the head node needs to be removed
        if length == n:
            return head.next
        
        # Step 3: Traverse to the (length - n)th node
        prev = None
        curr = head
        for _ in range(length - n):
            prev = curr
            curr = curr.next
        
        # Step 4: Remove the nth node by updating the pointers
        prev.next = curr.next
        
        return head