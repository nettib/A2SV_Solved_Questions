class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build the graph
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS
        visited = set()

        def dfs(node):
            if node == destination:
                return True

            visited.add(node)
            for nei in graph[node]:
                if nei in visited:
                    continue
                if dfs(nei):
                    return True
            return False

        return dfs(source)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna