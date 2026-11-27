# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -float("inf")

        def pathSumMax(node):
            nonlocal maxSum
            if not node:
                return 0
            
            left_sum = max(0, pathSumMax(node.left))
            right_sum = max(0, pathSumMax(node.right))

            maxSum = max(maxSum, left_sum + node.val + right_sum)

            return node.val + max(left_sum, right_sum)

        pathSumMax(root)
        return maxSum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna