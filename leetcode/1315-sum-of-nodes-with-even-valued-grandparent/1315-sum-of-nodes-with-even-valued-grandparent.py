# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        cum = 0
        def dfs(gp, p, node):
            nonlocal cum
            if not node:
                return
            
            if gp and gp.val % 2 == 0:
                cum += node.val
            
            dfs(p, node, node.left)
            dfs(p, node, node.right)
        
        dfs(None, None, root)
        return cum

