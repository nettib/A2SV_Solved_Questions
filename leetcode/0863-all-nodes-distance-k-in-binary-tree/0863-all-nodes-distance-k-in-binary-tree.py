# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
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
        
        q = deque([target.val])
        visited = set([target.val])

        ans = []
        while q:
            k -= 1
            for _ in range(len(q)):
                node = q.popleft()

                for nei in graph[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)

                    if not k:
                        ans.append(nei)
            
            if not k:
                return ans
    
        
        return ans
            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna