# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def getMax(node):
            while node.right:
                node = node.right
            return node
        
        def delete_node(root, key):
            if not root:
                return
            
            if key < root.val:
                root.left = delete_node(root.left, key)
            elif key > root.val:
                root.right = delete_node(root.right, key)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    temp = getMax(root.left)
                    root.val = temp.val
                    root.left = delete_node(root.left, temp.val)
            
            return root

        return delete_node(root, key)

            
