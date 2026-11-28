# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode | None:
        def get_max(nums):
            _max = [-1, -1]
            for i, num in enumerate(nums):
                if num > _max[-1]:
                    _max[0], _max[-1] = i, num
            
            return _max

        def dfs(nums):
            if not nums:
                return

            i, num = get_max(nums)
            node = TreeNode(num)

            node.left = dfs(nums[:i])
            node.right = dfs(nums[i + 1:])

            return node
        
        return dfs(nums)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna