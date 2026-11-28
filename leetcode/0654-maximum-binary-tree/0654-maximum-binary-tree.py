# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        stack = []
        root = TreeNode(-1)

        for i in range(len(nums)):
            node = TreeNode(nums[i])

            if node.val > root.val:
                root = node

            if not stack:
                stack.append(node)
                continue
            
            if stack[-1].val > nums[i]:
                stack[-1].right = node
                stack.append(node)
                continue

            while stack and stack[-1].val < nums[i]:
                prev = stack.pop()
            
            if stack:
                stack[-1].right = node
                
            node.left = prev
            stack.append(node)
        
        return root
        




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna