# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        graph = defaultdict(list)

        def dfs(node):
            if not node:
                return
            
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
                dfs(node.right)
            
        dfs(root)
        
        q = deque([start])
        visited = set([start])
        t = -1

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for nei in graph[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)
                
            t += 1
        
        return t



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna