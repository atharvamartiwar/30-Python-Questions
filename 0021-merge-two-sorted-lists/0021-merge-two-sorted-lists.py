# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Check if either list is empty
        if not list1:
            return list2
        if not list2:
            return list1
        
        # Create a dummy node as the head of the merged list
        dummy = ListNode()
        # Pointer to the current node in the merged list
        curr = dummy
        
        # Traverse both lists and compare the values of the nodes
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        # Append the remaining nodes from either list
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        
        return dummy.next