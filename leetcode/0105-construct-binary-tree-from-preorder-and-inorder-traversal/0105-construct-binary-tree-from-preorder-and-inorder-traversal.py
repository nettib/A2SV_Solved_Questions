# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map_idx = {val: i for i, val in enumerate(inorder)}
        p = 0

        def build(left, right):
            nonlocal p
            if left > right:
                return None

            root_val = preorder[p]
            p += 1
            root = TreeNode(root_val)

            mid = map_idx[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)