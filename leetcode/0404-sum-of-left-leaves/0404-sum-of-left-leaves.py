# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        _sum = 0
        def dfs(node, marker):
            nonlocal _sum
            if not node:
                return 
            
            if marker and not node.left and not node.right:
                _sum += node.val
                return 
            else:
                dfs(node.left, 1)
                dfs(node.right, 0)
        
        dfs(root, 0)

        return _sum
            
            