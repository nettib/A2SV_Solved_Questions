# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        q = deque([[None, None, root]])

        cum = 0
        while q:
            gp, p, node = q.popleft()

            if gp and gp.val % 2 == 0:
                cum += node.val
            
            if node.left:
                q.append([p, node, node.left])
            if node.right:
                q.append([p, node, node.right])
        
        return cum
            

            


        