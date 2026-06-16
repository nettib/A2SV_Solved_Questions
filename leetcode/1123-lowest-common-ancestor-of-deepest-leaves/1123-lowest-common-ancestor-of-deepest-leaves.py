# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # (lca, h)
        def dfs(node):
            if not node:
                return (None, 0)
            
            left_lca, lh = dfs(node.left)
            right_lca, rh = dfs(node.right)

            if lh == rh:
                return (node, lh + 1)
            elif lh > rh:
                return (left_lca, lh + 1)
            else:
                return (right_lca, rh + 1)
        
        lca, h = dfs(root)

        return lca

            



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna