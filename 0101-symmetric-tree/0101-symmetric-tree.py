# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         def isMirror(node1, node2):
#             if not node1 and not node2:
#                 return True
#             if not node1 or not node2:
#                 return False
#             return (
#                 node1.val == node2.val
#                 and isMirror(node1.left, node2.right)
#                 and isMirror(node1.right, node2.left)
#             )
        
#         return isMirror(root, root)
from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([(root.left, root.right)])
        
        while queue:
            node1, node2 = queue.popleft()
            
            if not node1 and not node2:
                continue
            
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            queue.append((node1.left, node2.right))
            queue.append((node1.right, node2.left))
        
        return True