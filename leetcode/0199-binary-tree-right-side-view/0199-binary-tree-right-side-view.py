# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([ root ])

        while q:
            rightMost = None
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                rightMost = node
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(rightMost.val)

        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna