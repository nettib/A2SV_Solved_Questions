class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = [-1] * len(graph)

        def get_color(parent):
            if colors[parent] == 0:
                return 1
            else:
                return 0

        visited = set()

        def dfs(node):

            for nei in graph[node]:
                if nei in visited:
                    if colors[node] == colors[nei]:
                        return False
                else:
                    colors[nei] = get_color(node)
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