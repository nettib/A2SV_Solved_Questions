# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        ans = [root.val, 0]
        def dfs(node, row):
            nonlocal ans
            if not node:
                return None
            
            if row > ans[-1]:
                ans = [node.val, row]
            
            if node.left:
                dfs(node.left, row + 1)
            if node.right:
                dfs(node.right, row + 1)
        
        dfs(root, 0)

        return ans[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna