# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node, path):
            nonlocal ans

            path.append(node.val)

            if not node.left and not node.right:
                ans += int("".join(map(str, path)))
                path.pop()
                return

            if node.left:
                dfs(node.left, path)
            if node.right:
                dfs(node.right, path)

            path.pop()

        dfs(root, [])
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna