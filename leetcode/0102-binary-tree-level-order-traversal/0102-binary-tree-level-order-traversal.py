# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([root])
        ans = []

        while q:
            temp = []
            n = len(q)

            for _ in range(n):
                node = q.popleft()
                if not node:
                    continue
                temp.append(node.val)
                q.append(node.left)
                q.append(node.right)
            if temp:
                ans.append(temp)
        
        return ans


            

