# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = None
        def dfs(node):
            nonlocal first, second, prev
            if not node:
                return 
            
            dfs(node.left)
            #Do sth
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                    second = node
                second = node
            prev = node


            dfs(node.right)
        
        dfs(root)

        first.val, second.val = second.val, first.val
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna