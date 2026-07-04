# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        track = defaultdict(int)

        q = deque([root])
        d = 0
        while q:
            _sum = 0
            for _ in range(len(q)):
                node = q.popleft()

                _sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            track[d] = _sum
            d += 1

        def dfs(node, d):
            if not node:
                return root
            
            _sum = 0
            if node.left:
                _sum += node.left.val
            if node.right:
                _sum += node.right.val
            
            if node.left:
                node.left.val = track[d] - _sum
            if node.right:
                node.right.val = track[d] - _sum
            
            dfs(node.left, d + 1)
            dfs(node.right, d + 1)
        
        dfs(root, 1)
        root.val = 0

        return root
            

                





# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna