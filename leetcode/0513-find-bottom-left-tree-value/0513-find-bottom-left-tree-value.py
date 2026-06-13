# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        ans = None

        while q:
            flag = 0
            for _ in range(len(q)):
                node = q.popleft()

                if not flag:
                    ans = node.val
                    flag += 1
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna