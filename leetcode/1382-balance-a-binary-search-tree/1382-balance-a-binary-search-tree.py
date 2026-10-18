# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        order = []

        def dfs(node):
            if not node:
                return 
            
            dfs(node.left)
            order.append(node.val)
            dfs(node.right)
        
        dfs(root)
        
        def build_bst(curr):
            if len(curr) == 0:
                return
            
            m = 0 + ((len(curr) - 0) // 2)

            node = TreeNode(val=curr[m])

            node.left = build_bst(curr[:m])
            node.right = build_bst(curr[m + 1:])
        
            return node
        
        return build_bst(order)
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna