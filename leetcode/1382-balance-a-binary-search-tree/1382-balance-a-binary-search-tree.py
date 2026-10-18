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
        
        def build_bst(curr, l, r):
            if l > r:
                return
            
            m = l + ((r - l) // 2)

            node = TreeNode(val=curr[m])

            node.left = build_bst(curr, l, m - 1)
            node.right = build_bst(curr, m + 1, r)
        
            return node
        
        return build_bst(order, 0, len(order) - 1)
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna