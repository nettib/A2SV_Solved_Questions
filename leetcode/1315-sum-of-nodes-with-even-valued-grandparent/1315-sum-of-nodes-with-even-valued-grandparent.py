# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        _sum = 0
        def dfs(node, parent, gparent):
            nonlocal _sum

            if not node:
                return 

            if gparent and gparent.val % 2 == 0:
                _sum += node.val
            
            dfs(node.left, node, parent)
            dfs(node.right, node, parent)
        
        dfs(root, None, None)
        return _sum
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna