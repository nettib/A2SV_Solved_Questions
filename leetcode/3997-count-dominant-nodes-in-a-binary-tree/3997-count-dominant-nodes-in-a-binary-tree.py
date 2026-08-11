# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        count = 0

        def dfs(node):
            nonlocal count
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            _max = max(node.val, left, right)

            if _max == node.val:
                count += 1
            
            return _max
        
        dfs(root)

        return count



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna