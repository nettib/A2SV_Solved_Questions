# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def tree_to_graph(node, parent):
            if not node:
                return

            if parent:
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)

            tree_to_graph(node.left, node)
            tree_to_graph(node.right, node)

        tree_to_graph(root, None)

        q = deque([target.val])
        visited = {target.val}
        ans = []

        while q:
            k -= 1
            for _ in range(len(q)):
                node = q.popleft()
                if k < 0:
                    ans.append(node)

                for nei in graph[node]:
                    if nei in visited:
                        continue
                    visited.add(nei)
                    q.append(nei)

            if k < 0:
                return ans

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna