# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        track = {0: 1}
        count = 0
    
        def dfs(node, _sum, targetSum):
            nonlocal count
            if not node:
                return 

            _sum += node.val
            if _sum - targetSum in track:
                count += (track[_sum - targetSum])
            
            if _sum not in track:
                track[_sum] = 0
            track[_sum] += 1
            
            dfs(node.left, _sum, targetSum)
            dfs(node.right, _sum, targetSum)
            track[_sum] -= 1
        
        dfs(root, 0, targetSum)
        return count







        