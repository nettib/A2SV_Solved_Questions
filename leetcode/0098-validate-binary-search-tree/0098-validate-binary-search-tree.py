# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validateBST(node, lb, ub):
            if not node:
                return True
            
            if node.val <= lb or node.val >= ub:
                return False
            
            return (validateBST(node.left, lb, min(ub, node.val)) and 
                    validateBST(node.right, max(lb, node.val), ub))
        
        return validateBST(root, -float("inf"), float("inf"))