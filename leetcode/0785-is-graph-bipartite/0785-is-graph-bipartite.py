class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)

        visited = set()

        def dfs(node):

            for nei in graph[node]:
                if nei in visited:
                    if colors[node] == colors[nei]:
                        return False
                else:
                    colors[nei] = 1 - colors[node]
                    visited.add(nei)
                    if not dfs(nei):
                        return False

            return True

        for node in range(len(graph)):
            if node not in visited:
                colors[node] = 0
                visited.add(node)
                if not dfs(node):
                    return False

        return True




# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna